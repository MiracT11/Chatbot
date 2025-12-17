import openpyxl
import re
from rapidfuzz import process, fuzz


def temizle(text):
    if text is None:
        return ""
    text = str(text).strip().lower()
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('\xa0', ' ')
    return text


workbook = openpyxl.load_workbook("sorular.xlsx")
sheet = workbook.active

qa_dict = {}
for row in sheet.iter_rows(min_row=2, values_only=True):
    soru_clean = temizle(row[0])
    cevap_clean = str(row[1]).strip() if row[1] else ""
    qa_dict[soru_clean] = cevap_clean


def get_answer(user_input, show_scores=False, min_score=60): 
    user_input = temizle(user_input)
    en_yakinlar = process.extract(
        user_input,
        qa_dict.keys(),
        scorer=fuzz.WRatio,
        limit=1
    )

    if en_yakinlar:
        soru, score, _ = en_yakinlar[0]
        if score >= min_score:
            if show_scores:
                return f"{soru} (benzerlik: {score}%)\nCevap: {qa_dict[soru]}"
            else:
                return qa_dict[soru]
        else:
            return "Üzgünüm, bu soruya cevap veremem."
    else:
        return "Üzgünüm, bu soruya cevap veremem."


if __name__ == "__main__":
    print("Chatbot başlatıldı! (Çıkmak için 'q' yazın)\n")
    while True:
        user_input = temizle(input("Bir soru sor: "))
        if user_input == "q":
            print("Çıkış yapılıyor... Görüşmek üzere!")
            break
        print("\nBulunan en yakın eşleşme:")
        print(get_answer(user_input, show_scores=True))
