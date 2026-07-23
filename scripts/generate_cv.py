"""Generate an updated professional CV PDF for Ali Haider Talukder Akib.

All external references (email, portfolio, GitHub, LinkedIn, competitive-programming
profiles, project repos) are rendered as working, blue, clickable hyperlinks.
"""
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_RIGHT
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
LINK = "#1a56db"  # blue for hyperlinks

# ---- canonical links (extracted from the original CV) ----
URLS = {
    "email": "mailto:alihaiderakib@gmail.com",
    "phone": "tel:+8801796620959",
    "portfolio": "https://akib1050.github.io/portfolio/",
    "github": "https://github.com/akib1050",
    "linkedin": "https://www.linkedin.com/in/ali-haider-talukder-akib-60274a19b/",
    "codeforces": "https://codeforces.com/profile/_akiib",
    "codechef": "https://www.codechef.com/users/ali_haider_007",
    "hackerrank": "https://www.hackerrank.com/Ali_Haider_Akib",
    "medicaid": "https://github.com/akib1050/MedicAid01",
}


def link(text, url):
    """Return an inline blue, underlined, clickable hyperlink."""
    return f'<a href="{url}" color="{LINK}"><u>{text}</u></a>'


def styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=19,
            textColor=INK, leading=22, alignment=TA_CENTER, spaceAfter=2,
        ),
        "title": ParagraphStyle(
            "TitleLine", parent=base["Normal"], fontName="Helvetica", fontSize=10.5,
            textColor=ACCENT, leading=13, alignment=TA_CENTER, spaceAfter=4,
        ),
        "contact": ParagraphStyle(
            "Contact", parent=base["Normal"], fontName="Helvetica", fontSize=8.6,
            textColor=MUTED, leading=12.5, alignment=TA_CENTER, spaceAfter=1,
        ),
        "h": ParagraphStyle(
            "Section", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=9.8,
            textColor=ACCENT, leading=11.5, spaceBefore=4.5, spaceAfter=2,
        ),
        "body": ParagraphStyle(
            "Body", parent=base["Normal"], fontName="Helvetica", fontSize=8.7,
            textColor=INK, leading=11.5, alignment=TA_JUSTIFY, spaceAfter=2,
        ),
        "role": ParagraphStyle(
            "Role", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=9.1,
            textColor=INK, leading=11,
        ),
        "meta_r": ParagraphStyle(
            "MetaR", parent=base["Normal"], fontName="Helvetica", fontSize=8.2,
            textColor=MUTED, leading=11, alignment=TA_RIGHT,
        ),
        "meta": ParagraphStyle(
            "Meta", parent=base["Normal"], fontName="Helvetica-Oblique", fontSize=8.1,
            textColor=MUTED, leading=10, spaceAfter=1,
        ),
        "company": ParagraphStyle(
            "Company", parent=base["Normal"], fontName="Helvetica-Oblique", fontSize=8.6,
            textColor=MUTED, leading=10, spaceAfter=1,
        ),
        "bullet": ParagraphStyle(
            "Bullet", parent=base["Normal"], fontName="Helvetica", fontSize=8.4,
            textColor=INK, leading=11, leftIndent=10, bulletIndent=0, spaceAfter=1,
        ),
        "skill": ParagraphStyle(
            "Skill", parent=base["Normal"], fontName="Helvetica", fontSize=8.4,
            textColor=INK, leading=11.4, spaceAfter=1.2,
        ),
        "small": ParagraphStyle(
            "Small", parent=base["Normal"], fontName="Helvetica", fontSize=8.5,
            textColor=INK, leading=10.5, spaceAfter=1,
        ),
    }


CONTENT_W = 182 * mm
LEFT_W = 130 * mm
RIGHT_W = CONTENT_W - LEFT_W


def _two_col(left_flow, right_text, s):
    t = Table([[left_flow, Paragraph(right_text, s["meta_r"])]], colWidths=[LEFT_W, RIGHT_W])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


def section(title, s):
    return [
        Paragraph(title.upper(), s["h"]),
        HRFlowable(width="100%", thickness=1, color=RULE, spaceAfter=4),
    ]


def job(role, company, dates, bullets, s):
    items = [_two_col(Paragraph(role, s["role"]), dates, s), Paragraph(company, s["company"])]
    items += [Paragraph(f"&bull;&nbsp; {b}", s["bullet"]) for b in bullets]
    items.append(Spacer(1, 3))
    return KeepTogether(items)


def project(name_html, role, dates, tech, desc, s):
    left = Paragraph(f"<b>{name_html}</b> &nbsp;&middot;&nbsp; {role}", s["small"])
    return KeepTogether([
        _two_col(left, dates, s),
        Paragraph(f"<i>{tech}</i>", s["meta"]),
        Paragraph(f"&bull;&nbsp; {desc}", s["bullet"]),
        Spacer(1, 2.5),
    ])


def build():
    s = styles()
    story = []

    story.append(Paragraph("Ali Haider Talukder Akib", s["name"]))
    story.append(Paragraph("Software Engineer II &nbsp;&middot;&nbsp; Brain Station 23", s["title"]))
    sep = " &nbsp;&middot;&nbsp; "
    story.append(Paragraph(
        "Dhaka, Bangladesh" + sep + link("+880 1796-620959", URLS["phone"]) + sep
        + link("alihaiderakib@gmail.com", URLS["email"]),
        s["contact"],
    ))
    story.append(Paragraph(
        link("Portfolio", URLS["portfolio"]) + sep
        + link("GitHub", URLS["github"]) + sep
        + link("LinkedIn", URLS["linkedin"]) + sep
        + link("Codeforces", URLS["codeforces"]) + sep
        + link("CodeChef", URLS["codechef"]) + sep
        +         link("HackerRank", URLS["hackerrank"]),
        s["contact"],
    ))
    story.append(Spacer(1, 4))

    # Summary
    story += section("Professional Summary", s)
    story.append(Paragraph(
        "Software Engineer II at Brain Station 23 with a strong foundation in algorithms and data "
        "structures (1,200+ competitive programming problems solved). Specialize in building scalable "
        ".NET / Angular systems on Azure &mdash; delivering end-to-end features across backend, frontend, "
        "and databases for international clients.",
        s["body"],
    ))

    # Experience
    story += section("Experience", s)
    story.append(job(
        "Software Engineer II", "Brain Station 23", "Jun 2025 &ndash; Present",
        [
            "Lead end-to-end development on enterprise products &mdash; system design, backend, frontend, and database.",
            "Drive performance optimization and scalable architecture for international client platforms.",
            "Stack: ASP.NET, Angular, Azure, Redis, PostgreSQL, Docker.",
        ], s,
    ))
    story.append(job(
        "Software Engineer I", "Brain Station 23", "Dec 2024 &ndash; Jun 2025",
        [
            "Delivered critical features across backend services and frontend interfaces.",
            "Resolved complex integration challenges and improved overall system reliability.",
        ], s,
    ))
    story.append(job(
        "Associate Software Engineer", "Brain Station 23", "Jul 2024 &ndash; Dec 2024",
        [
            "Built production features and contributed to client deliveries using enterprise engineering practices.",
        ], s,
    ))

    # Projects
    story += section("Selected Projects", s)
    story.append(project(
        "RS Sjoliv", "Lead Developer", "Sep 2025 &ndash; Present",
        "ASP.NET &middot; Angular &middot; Azure &middot; Redis",
        "Spearheaded end-to-end development: system design, backend, frontend, and database. Implemented "
        "critical features, resolved integration challenges, and optimized performance for a scalable enterprise solution.",
        s,
    ))
    story.append(project(
        "Trygg B&aring;t", "Backend Engineer", "Sep 2025 &ndash; Present",
        "ASP.NET &middot; Azure",
        "Contribute to system design, API development, and feature implementation for a boat-safety platform.",
        s,
    ))
    story.append(project(
        "OF Platform", "Software Developer", "Mar 2025 &ndash; Present",
        "ASP.NET &middot; Angular &middot; PostgreSQL &middot; Docker &middot; Redis",
        "Architected scalable designs, optimized database structures, and engineered backend services with "
        "intuitive frontend interfaces &mdash; expanding operational capabilities and user experience.",
        s,
    ))
    story.append(project(
        "MedicAid &nbsp;[" + link("repo", URLS["medicaid"]) + "]", "Full-stack", "",
        "C# &middot; ASP.NET &middot; MS SQL &middot; JavaScript",
        "Hospital / doctor / patient management system with appointments, medical records, billing, and inventory.",
        s,
    ))

    # Skills
    story += section("Technical Skills", s)
    story.append(Paragraph("<b>Languages:</b> C#, JavaScript / TypeScript, Java, Python, C/C++, HTML, CSS", s["skill"]))
    story.append(Paragraph("<b>Frameworks &amp; Libraries:</b> ASP.NET / .NET, Angular, jQuery, Bootstrap", s["skill"]))
    story.append(Paragraph("<b>Cloud &amp; Data:</b> Microsoft Azure, MS SQL, PostgreSQL, Redis, Docker, Firebase", s["skill"]))
    story.append(Paragraph("<b>Practices:</b> REST APIs, System Design, Data Structures &amp; Algorithms, Git, OOP", s["skill"]))

    # Education
    story += section("Education", s)
    story.append(_two_col(
        Paragraph("<b>B.Sc. in Computer Science &amp; Engineering</b>", s["role"]),
        "Jul 2019 &ndash; Nov 2023", s,
    ))
    story.append(Paragraph(
        "Ahsanullah University of Science and Technology (AUST) &mdash; CGPA 3.46 / 4.00", s["company"],
    ))
    story.append(Paragraph(
        "Coursework: Operating Systems, Data Structures, Algorithms, Distributed Databases, "
        "Software Engineering, Computer Architecture, Java OOP.", s["small"],
    ))

    # Achievements
    story += section("Achievements &amp; Leadership", s)
    lines = [
        "<b>2024</b> &mdash; NCPC Regional Finalist (NCPC JU 2024).",
        "<b>2023&ndash;Present</b> &mdash; Judge &amp; Problem Setter, Intra AUST Programming Contest (authored problems); trained juniors on competitive programming.",
        "<b>2022</b> &mdash; Regional Finalist, IUPC AUST 2022 &nbsp;&middot;&nbsp; 1st Runner-up, Intra AUST (CodeCombat 1.0) &nbsp;&middot;&nbsp; 5th, Cefalo CodeFiesta 2022.",
        "<b>Competitive Programming:</b> 1,200+ problems solved; 8+ onsite and 100+ online contests. "
        + link("Codeforces _akiib", URLS["codeforces"]) + " (rating 1210, 125 contests); "
        + link("CodeChef ali_haider_007", URLS["codechef"]) + " (max 1602); "
        + link("HackerRank", URLS["hackerrank"]) + " Gold Badge in C++.",
    ]
    story += [Paragraph(f"&bull;&nbsp; {ln}", s["bullet"]) for ln in lines]

    # Co-curricular
    story += section("Co-Curricular Activities", s)
    story.append(Paragraph(
        "&bull;&nbsp; <b>2nd Runner-up</b>, Inter Software Football Tournament &nbsp;&middot;&nbsp; "
        "Participated in the Inter Software Table Tennis Tournament &nbsp;&middot;&nbsp; "
        "Active in inter-company sports representing Brain Station 23.",
        s["bullet"],
    ))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUT), pagesize=A4,
        leftMargin=14 * mm, rightMargin=14 * mm, topMargin=11 * mm, bottomMargin=10 * mm,
        title="Ali Haider Talukder Akib - CV", author="Ali Haider Talukder Akib",
    )
    doc.build(story)
    DOWNLOADS.write_bytes(OUT.read_bytes())
    print(f"Wrote: {OUT}")
    print(f"Wrote: {DOWNLOADS}")
    print(f"Size: {OUT.stat().st_size} bytes")


if __name__ == "__main__":
    build()
