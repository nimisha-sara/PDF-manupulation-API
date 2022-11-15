from PyPDF2 import PdfWriter, PdfReader, PdfFileMerger
import os


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

    if page_no > reader.numPages or page_no < 0:
        output['msg'] = f"Invalid page. Page must be <= {reader.numPages + 1}"
        return output
    if not check_angle(angle):
        output['msg'] = "Invalid angle, angle must be a multiple of 90"
        return output
    if not check_extention(filepath):
        output['msg'] += "Invalid file extension"
        return output

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


def pdf_merge(pdf_loc: list, save_loc: str, save_pdf: str = "merged"):
    output = {'filepath': "", 'msg': ""}
    pdf_loc = pdf_loc[1:-1].split(',')
    merge = PdfFileMerger()

    for _pdf in pdf_loc:
        if check_extention(_pdf):
            try:
                pdf_file = PdfReader(_pdf)
            except FileNotFoundError:
                output['msg'] = f"File path incorrect: '{_pdf}'"
                return output
            else:
                try:
                    merge.append(pdf_file)
                except Exception as e:
                    output['msg'] = e
                    return output
        else:
            output['msg'] = f"File is not a pdf: '{_pdf}'"
            return output

    if os.path.exists(save_loc):
        with open(save_loc+f"/{save_pdf}.pdf", "wb") as output_stream:
            try:
                merge.write(output_stream)
            except Exception as e:
                output['msg'] = e
    else:
        output['msg'] = f"Output file path incorrect: '{save_loc}'"
    output['filepath'] = f"{save_loc}/{save_pdf}.pdf"
    output['msg'] = "Merge Successfull!"
    return output
