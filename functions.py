from PyPDF2 import PdfWriter, PdfReader, PdfFileMerger


def check_extention(url):
    ext = url.split('.')[-1]
    return ext == 'pdf'


def check_angle(angle):
    return angle % 90 == 0


def pdf_rotation(angle: int, page_no: int, filepath: str):
    """
    To rotate a specific page of a pdf by a specific angle

    Args:
        angle (int): Angle to be rotated by (Multiple of 90)
        page_no (int): Page no to be rotated
        filepath (str): Location of pdf file
    """
    reader = PdfReader(filepath)
    writer = PdfWriter()
    page_no -= 1
    output = {'filepath': "", 'msg': ""}

    if page_no > reader.numPages or page_no <= 0:
        output['msg'] = "Invalid page"
    if not check_angle(angle):
        output['msg'] = "Invalid angle, angle must be a multiple of 90"
    if not check_extention(filepath):
        output['msg'] = "Invalid file extension"

    try:
        for pagenum in range(reader.numPages):
            page = reader.getPage(pagenum)
            if pagenum == page_no:
                page.rotateClockwise(angle)
            writer.addPage(page)
        output_path = '/'.join(filepath.split('/')[:-1]) + '/output.pdf'
        pdf_out = open(output_path, 'wb')
        writer.write(pdf_out)
        output['filepath'] = output_path
        output['msg'] = "Operation Successfull!"
    except Exception as e:
        output['msg'] = e
    return output


# pdf_rotation(90, 1, "C:/Users/nimis/Downloads/New folder (2)/sample.pdf")
