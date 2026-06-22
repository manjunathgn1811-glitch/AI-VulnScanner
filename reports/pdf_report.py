from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(target, risk):

    file_path = "exports/report.pdf"

    pdf = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Vulnerability Assessment Report",
            styles['Title']
        )
    )

    content.append(Spacer(1,20))

    content.append(
        Paragraph(
            f"Target : {target}",
            styles['BodyText']
        )
    )

    content.append(
        Paragraph(
            f"Risk Level : {risk}",
            styles['BodyText']
        )
    )

    pdf.build(content)

    return file_path