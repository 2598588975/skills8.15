#!/usr/bin/env python3
"""Generate deterministic regression prompts and score preservation and anti-routine rules."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def generate(case: dict, intensity: int) -> str:
    conflict = ""
    if case.get("narrative_needed") and intensity >= 2:
        conflict = f"场景确实需要时只保留一个未解释信息：{case['conflict']}。"
    viewing_logic = case.get("viewing_logic", f"摄影机被放置在{case['camera']}，不是场景外的常规旁观机位")
    visual_hierarchy = case.get("visual_hierarchy", "第一眼看见用户指定主体或单一关键物件，第二眼再发现人物动作，环境退居末级")
    temporal_hold = case.get("temporal_hold", "画面像来自一段固定观察中的一帧，动作保持微小、重复或迟疑，不急于解释结果")
    viewing = f"观看逻辑采用空间嵌入：{viewing_logic}。"
    if intensity >= 2:
        viewing += f"视觉锚点与观看顺序：{visual_hierarchy}。"
    if intensity >= 3:
        viewing += f"镜头滞留：{temporal_hold}。"
    if "无人" in case["scene_type"]:
        action_calibration = "动作校准：无人场景只保留正在停止或刚发生的空间痕迹，不凭空加入人物。"
    else:
        action_calibration = "动作校准：依据观看节奏选择过渡、重复、等待或动作结束后的滞留状态，不强行戏剧化。"
    hard_constraints = case.get("hard_constraints", [])
    if hard_constraints:
        constraint_lock = f"一级硬约束锁定：{'；'.join(hard_constraints)}。"
    else:
        constraint_lock = "一级硬约束锁定：主体、人数、地点、动作与画幅保持用户输入。"
    light_shape = case.get(
        "light_shape",
        "主光只覆盖人物面部、关键手势和视觉锚点；非叙事墙面、天花板与无关设备设为禁光区，背景亮度比主体降低约一至两档",
    )
    color_hierarchy = case.get(
        "color_hierarchy",
        "一个最大色块承载场景基调，一个中等面积承托色分离人物，再以不超过约10%的小强调色打断；色块面积与落点清楚，不平均灰化",
    )
    casting = case.get("casting", "")
    casting_sentence = f"人物参考与选角：{casting}。" if casting else ""
    reference_transfer = case.get("reference_transfer", "")
    reference_sentence = f"参考图空间色彩转译：{reference_transfer}。" if reference_transfer else ""
    exposure_target = case.get(
        "exposure_target",
        "默认浓色胶片响应下阴影约40%–65%、中间调约30%–50%、局部亮部约5%–15%；有角色时让眼睛、肤色、白色与关键手势处于饱满可读中间调，同时保持背景曝光层级",
    )
    positive = (
        f"{case['aspect']}，电影级图像，画面核心严格保持“{case['input']}”"
        f"{constraint_lock}"
        f"时间地点为{case['time_place']}。{casting_sentence}{case['identity_costume']}，{case['position_action']}，{case['gaze']}。"
        f"{viewing}{conflict}摄影机设计为{case['camera']}；{case['composition']}。"
        f"语义主体与视觉锚点分开处理，只保留一个凝视主导，避免人物、物件与环境平均争夺注意力。"
        f"时代与地域严格由输入决定；旧场所不自动改变人物年代，未指定地域时不添加外语标牌或国别符号。"
        f"{action_calibration}"
        f"{reference_sentence}光色蓝图：主光与环境光遵循真实来源：{case['light']}。控光关系明确禁光区与背景亮度：{light_shape}。"
        f"默认浓色胶片响应：复古不等于低饱和；除非一级硬约束明确要求去饱和，使用中高色彩密度、饱满中间调和至少一个色相清楚的连续主色场。"
        f"颜色控制为{case['colors']}，并明确落在人物、服装、布景、灯光或道具上；色块面积关系为{color_hierarchy}。"
        f"曝光目标为{exposure_target}。"
        f"材质呈现{case['materials']}。35mm负片—印片响应：主色具有饱满印片密度，肤色保留红黄细微变化，浓黑接受相邻主色的轻微染料偏色并仍可辨衣料层次，中间调饱满，高光柔和滚降并带极轻光化晕染，细至中等不规则颗粒，有限微反差与边缘锐度，不抬黑、不褪色、不做数字HDR。"
    )
    return f"【正向提示词】\n\n{positive}\n\n【负面约束】\n\n{case['negative']}，避免肢体错误、视线错位、物件穿模与文字乱码。"


def split_output(output: str) -> tuple[str, str]:
    positive, negative = output.split("【负面约束】", 1)
    return positive.replace("【正向提示词】", "", 1).strip(), negative.strip()


def main() -> int:
    root = repo_root()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, default=root / "tests/inputs.json")
    parser.add_argument("--expected", type=Path, default=root / "tests/expected_traits.json")
    parser.add_argument("--output", type=Path, default=root / "tests/regression_results/latest.json")
    parser.add_argument("--intensity", type=int, choices=(1, 2, 3), default=2)
    args = parser.parse_args()
    cases = json.loads(args.inputs.read_text(encoding="utf-8"))
    expected = json.loads(args.expected.read_text(encoding="utf-8"))
    results = []
    camera_openings = Counter()
    for case in cases:
        output = generate(case, args.intensity)
        positive, negative = split_output(output)
        kept = [token for token in case["subject_tokens"] if token in positive]
        preservation = len(kept) / len(case["subject_tokens"])
        hard_constraints = case.get("hard_constraints", [])
        hard_hits = [constraint for constraint in hard_constraints if constraint in positive]
        contradictions = [phrase for phrase in case.get("forbidden_positive_phrases", []) if phrase in positive]
        required_case_phrases = case.get("required_output_phrases", [])
        missing_case_phrases = [phrase for phrase in required_case_phrases if phrase not in positive]
        required_concepts = expected["positive_required_concepts"] + expected.get("intensity_required_concepts", {}).get(str(args.intensity), [])
        style_hits = [concept for concept in required_concepts if concept in positive]
        allowed_routines = set(case.get("allowed_routines", []))
        routines = [term for term in expected["fixed_routines_not_allowed_in_positive"] if term in positive and term not in allowed_routines]
        forbidden = [term for term in expected["global_forbidden_terms"] if term.lower() in output.lower()]
        format_ok = all(section in output for section in expected["required_sections"])
        camera_phrase = case["camera"].split("，", 1)[0]
        camera_openings[camera_phrase] += 1
        failures = []
        if preservation < expected["preservation_threshold"]:
            failures.append(f"核心保留不足：{kept}")
        if len(hard_hits) != len(hard_constraints):
            failures.append(f"一级硬约束缺失：{[item for item in hard_constraints if item not in hard_hits]}")
        if contradictions:
            failures.append(f"正向提示词与一级约束矛盾：{contradictions}")
        if missing_case_phrases:
            failures.append(f"案例特定转译短语缺失：{missing_case_phrases}")
        if len(style_hits) != len(required_concepts):
            failures.append(f"摄影/光线/色彩/材质字段缺失：{style_hits}")
        if routines:
            failures.append(f"正向提示词出现固定套路：{routines}")
        if forbidden:
            failures.append(f"出现禁止词：{forbidden}")
        if not format_ok:
            failures.append("输出段落格式错误")
        result = {"id": case["id"], "input": case["input"], "output": output, "preservation_score": round(preservation, 3), "hard_constraint_hits": hard_hits, "constraint_contradictions": contradictions, "case_phrase_missing": missing_case_phrases, "style_rule_hits": style_hits, "repeated_routine_detection": routines, "forbidden_term_detection": forbidden, "passed": not failures, "failure_reasons": failures}
        results.append(result)
        print(f"[{case['id']}] {'PASS' if result['passed'] else 'FAIL'} 保留={preservation:.2f} 硬约束={len(hard_hits)}/{len(hard_constraints)} 矛盾={contradictions or '无'} 风格命中={len(style_hits)} 套路={routines or '无'} 禁止词={forbidden or '无'}")
    overused = {phrase: count for phrase, count in camera_openings.items() if count > expected["max_single_camera_phrase_frequency"]}
    if overused:
        for result in results:
            result["passed"] = False
            result["failure_reasons"].append(f"摄影机短语重复过多：{overused}")
    summary = {"total": len(results), "passed": sum(item["passed"] for item in results), "failed": sum(not item["passed"] for item in results), "intensity": args.intensity, "overused_camera_phrases": overused}
    payload = {"summary": summary, "results": results}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"summary: {summary}; report: {args.output}")
    return 0 if summary["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
