from django.shortcuts import render
from fugashi import Tagger, GenericTagger
import jaconv
from PIL import Image
import pytesseract

# Create your views here.


# 使用 GenericTagger 初始化
tagger = GenericTagger()

# 指定 tesseract 可执行文件路径
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Windows


def home(request):
    """显示门户页面"""
    return render(request, "home.html")


def add_furigana(text):
    """
    为日文文章中的汉字加上平假名，并对动词的假名注释加红色。
    同时提取动词的原形到一个单独的列表。
    保留原文中的回车换行位置。
    """
    result = []
    verbs = []  # 用于存储动词的原形

    # 按行拆分文本，逐行处理
    for line in text.splitlines(keepends=True):  # 保留换行符
        line_result = []  # 存储每行的结果

        for word in tagger(line):
            features = word.feature  # 获取词的特征
            kana = features[7] if len(features) > 7 else None  # 获取假名
            pos = features[0] if len(features) > 0 else None  # 获取词性
            base_form = features[6] if len(features) > 6 else None  # 获取原形

            if kana and kana != word.surface:
                # 将片假名转为平假名
                hiragana = jaconv.kata2hira(kana)
                # 如果是动词，使用红色标记，并将原形添加到列表
                if pos == "動詞":
                    if base_form and base_form not in verbs:
                        verbs.append(base_form)
                    line_result.append(
                        f"<ruby>{word.surface}<rt><span style='color:red'>{hiragana}</span></rt></ruby>")
                else:
                    line_result.append(f"<ruby>{word.surface}<rt>{hiragana}</rt></ruby>")
            else:
                line_result.append(word.surface)

        # 将处理后的行内容加到结果中，包括行末换行符
        result.append(''.join(line_result))

    # 使用 <br> 替换换行符
    formatted_result = '<br>'.join(result)

    # 将动词原形列表去重并转换为前端可用的格式
    verbs_output = ', '.join(set(verbs))

    return formatted_result, verbs_output


def process_image(image_path):
    """从图片中提取日语文本并加注假名。"""
    try:
        # 使用 Tesseract OCR 读取图像中的文本
        image = Image.open(image_path).convert("RGB")  # 确保图片为 RGB 格式
        print("Image loaded successfully:", image)

        # 检查图像属性
        print("Image size:", image.size)
        print("Image mode:", image.mode)

        # 调整 Tesseract 配置
        custom_config = r'--oem 3 --psm 6'
        extracted_text = pytesseract.image_to_string(image, lang='jpn', config=custom_config)
        print("Extracted text:", extracted_text)

        if not extracted_text.strip():
            print("No text detected in the image.")
            return "图片中未检测到文本", ""

        # 调用 add_furigana 函数处理文本
        furigana_text, verbs_output = add_furigana(extracted_text)
        return furigana_text, verbs_output
    except Exception as e:
        # 捕获并打印异常堆栈信息
        import traceback
        traceback.print_exc()
        return f"图片处理失败: {e}", ""


def japan_kanji(request):
    """处理日文文本或图片上传，生成带假名注释的文本和动词原形列表。"""
    processed_text = ""
    verbs_output = ""

    if request.method == "POST":
        # 处理文本输入
        input_text = request.POST.get("input_text", "").strip()
        if input_text:
            processed_text, verbs_output = add_furigana(input_text)
        # 处理图片上传
        elif 'image_upload' in request.FILES:
            image_file = request.FILES["image_upload"]
            try:
                # 调用处理图片的函数
                processed_text, verbs_output = process_image(image_file)
            except Exception as e:
                processed_text = f"图片处理失败: {e}"
                verbs_output = ""

    return render(request, "jap_kanji.html", {"processed_text": processed_text, "verbs_output": verbs_output})


def jap_audio_rec(request):
    return render(request, 'jap_audio_rec.html')
