from manim import *

class Subsoal1_Geometri(Scene):
    def construct(self):
        # Judul
        judul = Text("Subsoal 1: Sketsa dan Hubungan Pythagoras", font_size=32)
        self.play(Write(judul))
        self.wait(1)
        self.play(judul.animate.to_edge(UP))
        self.wait(0.5)

        # Buat lingkaran
        lingkaran = Circle(radius=2, color=BLUE)
        lingkaran.shift(LEFT * 2)  # geser ke kiri agar ada ruang untuk titik P
        self.play(Create(lingkaran))
        self.wait(0.5)

        # Titik pusat O
        O = Dot(lingkaran.get_center(), color=WHITE)
        label_O = Text("O", font_size=24).next_to(O, DOWN+LEFT, buff=0.1)
        self.play(Create(O), Write(label_O))
        self.wait(0.3)

        # Titik P di kanan
        P_pos = lingkaran.get_center() + RIGHT * 5.2  # jarak OP = 5.2 unit (skala)
        P = Dot(P_pos, color=YELLOW)
        label_P = Text("P", font_size=24).next_to(P, DOWN+RIGHT, buff=0.1)
        self.play(Create(P), Write(label_P))
        self.wait(0.3)

        # Garis OP
        garis_OP = Line(O.get_center(), P.get_center(), color=YELLOW)
        self.play(Create(garis_OP))
        self.wait(0.5)

        # Titik singgung A (di atas) dan B (di bawah) pada lingkaran
        # Hitung sudut: sin(theta) = r/OP = 2/5.2, cos(theta) = sqrt(1 - (2/5.2)^2)
        # Untuk visual, kita letakkan A di sudut sekitar 30 derajat dari garis OP
        import math
        theta = math.acos(2/5.2)  # sudut antara OA dan OP
        # Arah dari O ke P adalah RIGHT, maka sudut dari sumbu x positif
        sudut_A = theta  # di atas
        sudut_B = -theta  # di bawah
        A_pos = lingkaran.get_center() + 2 * np.array([math.cos(sudut_A), math.sin(sudut_A), 0])
        B_pos = lingkaran.get_center() + 2 * np.array([math.cos(sudut_B), math.sin(sudut_B), 0])
        A = Dot(A_pos, color=GREEN)
        B = Dot(B_pos, color=GREEN)
        label_A = Text("A", font_size=24).next_to(A, UP, buff=0.1)
        label_B = Text("B", font_size=24).next_to(B, DOWN, buff=0.1)
        self.play(Create(A), Create(B), Write(label_A), Write(label_B))
        self.wait(0.5)

        # Garis singgung PA dan PB
        garis_PA = Line(P.get_center(), A.get_center(), color=GREEN)
        garis_PB = Line(P.get_center(), B.get_center(), color=GREEN)
        self.play(Create(garis_PA), Create(garis_PB))
        self.wait(0.5)

        # Segitiga siku-siku OAP: gambar sudut siku di A
        siku = RightAngle(Line(O.get_center(), A.get_center()), Line(A.get_center(), P.get_center()), length=0.3, color=RED)
        self.play(Create(siku))
        self.wait(0.5)

        # Teks persamaan Pythagoras
        eq_text = VGroup(
            Text("Pada segitiga siku-siku OAP:", font_size=26, color=YELLOW),
            MathTex("OP^2 = OA^2 + PA^2", font_size=36),
            MathTex("13^2 = 5^2 + PA^2", font_size=36)
        )
        eq_text.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        eq_text.next_to(lingkaran, RIGHT, buff=1)
        self.play(Write(eq_text[0]))
        self.wait(0.5)
        self.play(Write(eq_text[1]))
        self.wait(0.5)
        self.play(Write(eq_text[2]))
        self.wait(2)

        # Selesai
        self.play(FadeOut(judul, lingkaran, O, label_O, P, label_P, garis_OP, A, B, label_A, label_B, garis_PA, garis_PB, siku, eq_text))
        self.wait(1)