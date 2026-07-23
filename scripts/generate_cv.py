"""Generate an updated professional CV PDF for Ali Haider Talukder Akib."""
from pathlib import Path

from reportlab.lib.colors import HexColor, white
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUT = Path(r"C:\Akib Personal\Akib\assets\docs\Ali_Haider_Talukder_Akib_CV.pdf")
DOWNLOADS = Path(r"C:\Users\BS01329\Downloads\Ali_Haider_Talukder_Akib_CV_Updated.pdf")

INK = HexColor("#121826")
MUTED = HexColor("#4b5568")
ACCENT = HexColor("#3730a3")
RULE = HexColor("#c7cdd8")
LIGHT = HexColor("#f3f4f8")


def styles():
    base = getSampleStyleSheet()
    s = {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=20,
            textColor=INK,
            leading=24,
            alignment=TA_CENTER,
            spaceAfter=2,
        ),
        "title": ParagraphStyle(
            "TitleLine",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=11,
            textColor=ACCENT,
            leading=14,
            alignment=TA_CENTER,
            spaceAfter=6,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.5,
            textColor=MUTED,
            leading=12,
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        "h": ParagraphStyle(
            "Section",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            textColor=ACCENT,
            leading=13,
            spaceBefore=8,
            spaceAfter=3,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            textColor=INK,
            leading=12,
            alignment=TA_JUSTIFY,
            spaceAfter=4,
        ),
        "role": ParagraphStyle(
            "Role",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.5,
            textColor=INK,
            leading=12,
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.5,
            textColor=MUTED,
            leading=11,
        ),
        "meta_r": ParagraphStyle(
            "MetaR",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.5,
            textColor=MUTED,
            leading=11,
            alignment=TA_RIGHT,
        ),
        "company": ParagraphStyle(
            "Company",
            parent=base["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=9,
            textColor=MUTED,
            leading=11,
            spaceAfter=2,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.8,
            textColor=INK,
            leading=11.5,
            leftIndent=10,
            bulletIndent=0,
            spaceAfter=1.5,
        ),
        "skill": ParagraphStyle(
            "Skill",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.8,
            textColor=INK,
            leading=12,
            spaceAfter=2,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.5,
            textColor=INK,
            leading=11,
            spaceAfter=2,
        ),
    }
    return s


def section(title, s):
    return [
        Paragraph(title.upper(), s["h"]),
        HRFlowable(width="100%", thickness=1, color=RULE, spaceAfter=5),
    ]


def job(role, company, dates, bullets, s):
    head = Table(
        [[Paragraph(role, s["role"]), Paragraph(dates, s["meta_r"])]],
        colWidths=[125 * mm, 55 * mm],
    )
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    items = [head, Paragraph(company, s["company"])]
    for b in bullets:
        items.append(Paragraph(f"• {b}", s["bullet"]))
    items.append(Spacer(1, 4))
    return KeepTogether(items)


def project(name, tech, role, desc, s):
    head = Table(
        [[Paragraph(f"<b>{name}</b>", s["small"]), Paragraph(role, s["meta_r"])]],
        colWidths=[125 * mm, 55 * mm],
    )
    head.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    return KeepTogether(
        [
            head,
            Paragraph(f"<font color='#4b5568'><i>{tech}</i></font>", s["meta"]),
            Paragraph(desc, s["bullet"]),
            Spacer(1, 3),
        ]
    )


def build():
    s = styles()
    story = []

    story.append(Paragraph("Ali Haider Talukder Akib", s["name"]))
    story.append(Paragraph("Software Engineer II · Brain Station 23", s["title"]))
    story.append(
        Paragraph(
            "Dhaka, Bangladesh  ·  +880 1796-620959  ·  alihaiderakib@gmail.com<br/>"
            "Portfolio: akib1050.github.io/portfolio  ·  "
            "Codeforces: _akiib  ·  GitHub / LinkedIn available on request",
            s["contact"],
        )
    )

    # Summary
    story += section("Professional Summary", s)
    story.append(
        Paragraph(
            "Software Engineer II at Brain Station 23 with a strong foundation in algorithms and data "
            "structures (1,200+ competitive programming problems solved). Specialize in building scalable "
            ".NET / Angular systems on Azure, delivering end-to-end features across backend, frontend, and "
            "databases for international clients. Experienced judge and problem setter for university "
            "programming contests.",
            s["body"],
        )
    )

    # Experience
    story += section("Experience", s)
    story.append(
        job(
            "Software Engineer II",
            "Brain Station 23",
            "Jun 2025 — Present",
            [
                "Lead end-to-end development on enterprise products — system design, backend, frontend, and database.",
                "Drive performance optimization and scalable architecture for international client platforms.",
                "Tech: ASP.NET, Angular, Azure, Redis, PostgreSQL, Docker.",
            ],
            s,
        )
    )
    story.append(
        job(
            "Software Engineer I",
            "Brain Station 23",
            "Dec 2024 — Jun 2025",
            [
                "Delivered critical features across backend services and frontend interfaces.",
                "Resolved complex integration challenges and improved system reliability.",
            ],
            s,
        )
    )
    story.append(
        job(
            "Associate Software Engineer",
            "Brain Station 23",
            "Jul 2024 — Dec 2024",
            [
                "Built production features and contributed to client deliveries using enterprise engineering practices.",
            ],
            s,
        )
    )

    # Projects
    story += section("Selected Projects", s)
    story.append(
        project(
            "RS Sjoliv",
            "ASP.NET · Angular · Azure · Redis",
            "Lead Developer · Sep 2025 — Present",
            "Spearheaded end-to-end development: system design, backend, frontend, and database. Implemented "
            "critical features, resolved integration challenges, and optimized performance for a scalable enterprise solution.",
            s,
        )
    )
    story.append(
        project(
            "Trygg Båt",
            "ASP.NET · Azure",
            "Backend Engineer · Sep 2025 — Present",
            "Contribute to system design, API development, and feature implementation for a boat-safety platform.",
            s,
        )
    )
    story.append(
        project(
            "OF Platform",
            "ASP.NET · Angular · PostgreSQL · Docker · Redis",
            "Software Developer · Mar 2025 — Present",
            "Architected scalable designs, optimized database structures, and engineered backend services with "
            "intuitive frontend interfaces — expanding operational capabilities and UX.",
            s,
        )
    )
    story.append(
        project(
            "MedicAid",
            "C# · ASP.NET · MS SQL · JavaScript",
            "Full-stack",
            "Hospital / doctor / patient management system with appointments, records, billing, and inventory.",
            s,
        )
    )

    # Skills
    story += section("Technical Skills", s)
    story.append(
        Paragraph(
            "<b>Languages:</b> C#, JavaScript / TypeScript, Java, Python, C/C++, HTML, CSS",
            s["skill"],
        )
    )
    story.append(
        Paragraph(
            "<b>Frameworks &amp; Libraries:</b> ASP.NET / .NET, Angular, jQuery, Bootstrap",
            s["skill"],
        )
    )
    story.append(
        Paragraph(
            "<b>Cloud &amp; Data:</b> Microsoft Azure, MS SQL, PostgreSQL, Redis, Docker, Firebase",
            s["skill"],
        )
    )
    story.append(
        Paragraph(
            "<b>Practices:</b> REST APIs, System Design, Data Structures &amp; Algorithms, Git, OOP",
            s["skill"],
        )
    )

    # Education
    story += section("Education", s)
    edu = Table(
        [
            [
                Paragraph("<b>B.Sc. in Computer Science &amp; Engineering</b>", s["role"]),
                Paragraph("Jul 2019 — Nov 2023", s["meta_r"]),
            ]
        ],
        colWidths=[125 * mm, 55 * mm],
    )
    edu.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    story.append(edu)
    story.append(
        Paragraph(
            "Ahsanullah University of Science and Technology (AUST) — CGPA 3.46 / 4.00",
            s["company"],
        )
    )
    story.append(
        Paragraph(
            "Coursework: Operating Systems, Data Structures, Algorithms, Distributed Databases, "
            "Software Engineering, Computer Architecture, Java OOP.",
            s["small"],
        )
    )

    # Achievements
    story += section("Achievements &amp; Leadership", s)
    for line in [
        "<b>2024</b> — NCPC Regional Finalist (NCPC JU 2024).",
        "<b>2023–Present</b> — Judge &amp; Problem Setter, Intra AUST Programming Contest; authored contest problems.",
        "<b>2022</b> — Regional Finalist, IUPC AUST 2022.",
        "<b>2022</b> — 1st Runner-up, Intra AUST Programming Contest (CodeCombat 1.0).",
        "<b>2022</b> — 5th place, Cefalo CodeFiesta 2022 (Intra AUST Segments).",
        "<b>Competitive programming:</b> 1,200+ problems solved; 8+ onsite and 100+ online contests. "
        "Codeforces <b>_akiib</b> (rating 1210, 125 contests); CodeChef <b>ali_haider_007</b> (max 1602); "
        "HackerRank Gold Badge in C++.",
        "Trained juniors on competitive programming (2022–23).",
    ]:
        story.append(Paragraph(f"• {line}", s["bullet"]))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=14 * mm,
        rightMargin=14 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm,
        title="Ali Haider Talukder Akib — CV",
        author="Ali Haider Talukder Akib",
    )
    doc.build(story)
    DOWNLOADS.write_bytes(OUT.read_bytes())
    print(f"Wrote: {OUT}")
    print(f"Wrote: {DOWNLOADS}")
    print(f"Size: {OUT.stat().st_size} bytes")


if __name__ == "__main__":
    build()
