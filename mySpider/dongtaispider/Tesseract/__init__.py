#要运行这个包下面的程序要装Tesseract
#Windows 系统
# 下载可执行安装文件https://code.google.com/p/tesseract-ocr/downloads/list安装。
#
# Linux 系统
# 可以通过 apt-get 安装: $sudo apt-get tesseract-ocr


#配置环境
# 要使用 Tesseract 的功能，比如后面的示例中训练程序识别字母，
# 要先在系统中设置一 个新的环境变量 $TESSDATA_PREFIX，
# 让 Tesseract 知道训练的数据文件存储在哪里，
# 然后搞一份tessdata数据文件，放到Tesseract目录下。
# 在大多数 Linux 系统和 Mac OS X 系统上,你可以这么设置: $export TESSDATA_PREFIX=/usr/local/share/Tesseract
#
# 在 Windows 系统上也类似,你可以通过下面这行命令设置环境变量: #setx TESSDATA_PREFIX C:\Program Files\Tesseract OCR\Tesseract
#
# 安装pytesseract
# Tesseract 是一个 Python 的命令行工具，不是通过 import 语句导入的库。安装之后,要用 tesseract 命令在 Python 的外面运行，但我们可以通过 pip 安装支持Python 版本的 Tesseract库：
#
# pip install pytesseract