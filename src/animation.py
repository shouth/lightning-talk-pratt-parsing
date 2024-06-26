from manim import *
from manim_slides.slide import Slide

Tex.set_default(tex_template=TexTemplate(
    tex_compiler = "lualatex",
    output_format = ".pdf",
    preamble = r"""
        \usepackage{amsmath}
        \usepackage{amssymb}
        \usepackage{luatexja}
        \usepackage[haranoaji]{luatexja-preset}
    """
))

MathTex.set_default(tex_template=TexTemplate(
    tex_compiler = "lualatex",
    output_format = ".pdf",
    preamble = r"""
        \usepackage{amsmath}
        \usepackage{amssymb}
        \usepackage{luatexja}
        \usepackage[haranoaji]{luatexja-preset}
    """
))

class AquatanSlide(Slide):
    def construct(self):
        title = Text("式を解釈するアルゴリズムの話", font_size=60)

        self.play(Write(title))
        self.next_slide()

        example_exp_original = MathTex(
            "10 - 2 \\times 3 + 7",
        )

        example_exp = example_exp_original.copy()

        self.play(FadeOut(title))
        self.play(Write(example_exp))

        self.next_slide()

        example_exp_with_ans = MathTex(
            "10 - 2 \\times 3 + 7", "= 11",
        )
        self.play(
            Transform(example_exp, example_exp_with_ans),
        )

        self.next_slide()

        self.play(
            example_exp.animate.shift(UP),
        )

        example_exp_paren_0 = MathTex("10 - (2 \\times (3 + 7)) = -10")
        example_exp_paren_1 = MathTex("(10 - 2) \\times (3 + 7) = 80")
        example_exp_paren_0.next_to(example_exp, DOWN)
        example_exp_paren_1.next_to(example_exp_paren_0, DOWN)

        self.play(
            FadeIn(example_exp_paren_0),
            FadeIn(example_exp_paren_1))

        self.next_slide()

        self.play(
            FadeOut(example_exp_paren_0),
            FadeOut(example_exp_paren_1))

        example_exp_with_paren = MathTex(
            "10 - (2 \\times 3) + 7", "= 11",
        )
        self.play(
            Transform(example_exp, example_exp_with_paren),
        )

        self.next_slide()
        self.play(
            Transform(example_exp, example_exp_original),
        )

        next_example_exp = MathTex(
            "10", "-", "2", "\\times", "3", "+", "7",
        )

        term = Text("項", font_size=40, color=RED)
        operator = Text("演算子", font_size=40, color=BLUE)
        term.next_to(next_example_exp, UP)
        operator.next_to(next_example_exp, DOWN)
        self.play(
            FadeOut(example_exp),
            next_example_exp[0].animate.set_color(RED),
            next_example_exp[1].animate.set_color(BLUE),
            next_example_exp[2].animate.set_color(RED),
            next_example_exp[3].animate.set_color(BLUE),
            next_example_exp[4].animate.set_color(RED),
            next_example_exp[5].animate.set_color(BLUE),
            next_example_exp[6].animate.set_color(RED),
            FadeIn(term),
            FadeIn(operator),
        )
        example_exp = next_example_exp

        self.next_slide()
        self.play(
            example_exp.animate.set_color(GREY_D),
            FadeOut(term),
            FadeOut(operator),
        )

        self.next_slide()
        next_example_exp = MathTex(
            "10", "-", "2", "\\times", "3", "+", "7",
        )
        next_example_exp.set_color(GREY_D)

        self.play(
            next_example_exp[0].animate.set_color(YELLOW),
            # Transform(example_exp, next_example_exp),
        )
        example_exp = next_example_exp

        self.next_slide()
        self.play(
            example_exp.animate.set_color_by_tex_to_color_map({
                "10": RED,
                "-": BLUE,
                "2": RED,
            }),
        )

        self.next_slide()

        next_example_exp = MathTex(
            "{{8}} {{\\times 3 + 7}}",
        )
        next_example_exp.set_color(GREY_D)
        next_example_exp.set_color_by_tex("8", YELLOW)
        self.play(
            Transform(example_exp, next_example_exp),
        )

        self.next_slide()

        next_example_exp = MathTex(
            "{{8}} \\times {{3}} {{+ 7}}",
        )
        next_example_exp.set_color(GREY_D)
        next_example_exp.set_color_by_tex("8", YELLOW)

        self.play(
            FadeOut(example_exp),
            next_example_exp.animate.set_color_by_tex_to_color_map({
                "8": RED,
                "\\times": BLUE,
                "3": RED,
            }),
        )
        example_exp = next_example_exp

        self.next_slide()

        next_example_exp = MathTex(
            "{{24}} {{+ 7}}",
        )
        next_example_exp.set_color(GREY_D)
        next_example_exp.set_color_by_tex("24", YELLOW)

        self.play(
            Transform(example_exp, next_example_exp),
        )

        self.next_slide()

        next_example_exp = MathTex(
            "{{24}} + {{7}}",
        )
        next_example_exp.set_color(GREY_D)
        next_example_exp.set_color_by_tex("24", YELLOW)

        self.play(
            FadeOut(example_exp),
            next_example_exp.animate.set_color_by_tex_to_color_map({
                "24": RED,
                "+": BLUE,
                "7": RED,
            }),
        )
        example_exp = next_example_exp

        self.next_slide()

        next_example_exp = MathTex(
            "{{}} {{31}}",
        )
        next_example_exp.set_color(YELLOW)

        self.play(
            Transform(example_exp, next_example_exp),
        )

        self.next_slide()

        next_example_exp = MathTex(
            "{{10 - 2 \\times 3 + 7 =}} {{31}}",
        )

        self.play(
            Transform(example_exp, next_example_exp),
        )

        self.next_slide()

        next_example_exp = MathTex(
            "{{((10 - 2) \\times 3) + 7 =}} {{31}}",
        )

        self.play(
            Transform(example_exp, next_example_exp),
        )

        self.next_slide()
        self.play(
            FadeOut(example_exp),
        )

        simple_calculator = Code(
            file_name="simple_calculator.py",
            language="python",
            tab_width=4,
            font_size=14,
            insert_line_no=False,
        )

        self.play(
            FadeIn(simple_calculator),
        )

        self.next_slide()
        self.play(FadeOut(simple_calculator))

        rules = [
            [r"\text{式}", r"& :=", r"\text{乗除式}", r"\ |", r"\ \text{乗除式}", r"\ \text{加法演算子}", r"\ \text{式} \\"],
            [r"\text{加法演算子}", r"& :=", r"+", r"\ |", r"\ - \\"],
            [r"\text{乗除式}", r"& :=", r"\text{項}", r"\ |", r"\ \text{項}", r"\ \text{乗法演算子}", r"\ \text{乗除式} \\"],
            [r"\text{乗法演算子}", r"& :=", r"\times", r"\ |", r"\ \slash \\"],
            [r"\text{項}", r"& :=", r"\text{'数字を1回以上並べたもの'}"]
        ]
        rules_offsets = [0]
        for rule in rules:
            rules_offsets.append(rules_offsets[-1] + len(rule))

        rule = MathTex(*sum(rules, []))
        self.play(FadeIn(rule))

        self.next_slide()

        exp = MathTex(
            "10", "-", "2", "\\times", "3", "+", "7",
        )
        self.play(
            rule.animate.scale(0.6).to_edge(LEFT).shift(RIGHT),
        )
        exp.next_to(rule, RIGHT)
        exp.shift(RIGHT)
        self.play(
            Write(exp),
        )

        self.next_slide()
        self.play(
            rule[rules_offsets[0]:rules_offsets[1]].animate.set_color(RED),
        )

        self.next_slide()
        self.play(
            rule[2].animate.set_color(BLUE),
            rule[4].animate.set_color(BLUE),
            rule[rules_offsets[2]:rules_offsets[3]].animate.set_color(BLUE),
        )

        self.next_slide()
        self.play(
            rule[rules_offsets[2] + 2].animate.set_color(YELLOW),
            rule[rules_offsets[2] + 4].animate.set_color(YELLOW),
            rule[rules_offsets[4]:rules_offsets[5]].animate.set_color(YELLOW),
        )

        self.next_slide()
        self.play(
            exp[0].animate.set_color(YELLOW),
        )

        self.next_slide()
        self.play(
            rule[rules_offsets[2] + 2].animate.set_color(BLUE),
            rule[rules_offsets[2] + 4].animate.set_color(BLUE),
            rule[rules_offsets[2] + 5].animate.set_color(ORANGE),
            rule[rules_offsets[3]:rules_offsets[4]].animate.set_color(ORANGE),
            rule[rules_offsets[4]:rules_offsets[5]].animate.to_original_color(),
        )

        self.next_slide()
        self.play(
            rule[2].animate.set_color(RED),
            rule[4].animate.set_color(RED),
            rule[5].animate.set_color(GREEN),
            rule[rules_offsets[1]:rules_offsets[2]].animate.set_color(GREEN),
            rule[rules_offsets[2]:rules_offsets[3]].animate.to_original_color(),
            rule[rules_offsets[3]:rules_offsets[4]].animate.to_original_color(),
        )

        self.next_slide()
        self.play(
            exp[1].animate.set_color(GREEN),
        )
