import random

def main():
    hiragana = {"a":"あ","i":"い","u":"う", "e":"え", "o":"お",
        "ka":"か","ki":"き","ku":"く", "ke":"け", "ko":"こ",
        "sa":"さ","shi":"し","su":"す", "se":"せ", "so":"そ",
        "ta":"た","chi":"ち","tsu":"つ", "te":"て", "to":"と",
        "na":"な","ni":"に","nu":"ぬ", "ne":"ね", "no":"の",
        "ha":"は","hi":"ひ","fu":"ふ", "he":"へ", "ho":"ほ",
        "ma":"ま","mi":"み","mu":"む", "me":"め", "mo":"も",
        "ra":"ら","ri":"り","ru":"る", "re":"れ", "ro":"ろ",
        "ya":"や","yu":"ゆ", "yo":"よ",
        "wa":"わ", "(w)o":"を", "n":"ん"}

    katakana = {"a":"ア","i":"イ","u":"ウ", "e":"エ", "o":"オ",
        "ka":"カ","ki":"キ","ku":"ク", "ke":"ケ", "ko":"コ",
        "sa":"サ","shi":"シ","su":"ス", "se":"セ", "so":"ソ",
        "ta":"タ","chi":"チ","tsu":"ツ", "te":"テ", "to":"ト",
        "na":"ナ","ni":"ニ","nu":"ヌ", "ne":"ネ", "no":"ノ",
        "ha":"ハ","hi":"ヒ","fu":"フ", "he":"ヘ", "ho":"ホ",
        "ma":"マ","mi":"ミ","mu":"ム", "me":"メ", "mo":"モ",
        "ra":"ラ","ri":"リ","ru":"ル", "re":"レ", "ro":"ロ",
        "ya":"ヤ","yu":"ユ", "yo":"ヨ",
        "wa":"ワ", "(w)o":"ヲ", "n":"ン"}
    
    kanji = {"ichi (1)":"一", "ni (2)":"二", "san (3)":"三", "yon/shi (4)":"四", "go (5)":"五",
        "roku (6)":"六", "nana/shichi (7)":"七", "hachi (8)":"八", "kyu/ku (9)":"九", "juu (10)":"十",
        "ko (child)":"子", "watashi (I, me)":"私"}

    alphabet = input("hiragana, katanana, or kanji?\n")
    
    cont = True

    while(cont):
        key,val = "Error, incorrect input", "0"
        if alphabet == "hiragana":
            key,val = random.choice(list(hiragana.items()))
        elif alphabet == "katakana":
            key,val = random.choice(list(katakana.items()))
        elif alphabet == "kanji":
            key,val = random.choice(list(kanji.items()))
        print(key)
        check = input("\nCheck answer?\n")
        print(val)
        temp_cont = input("\nContinue practice? (Y/n)\n")
        if temp_cont == "n":
            cont = False




if __name__ == "__main__":
    main()
