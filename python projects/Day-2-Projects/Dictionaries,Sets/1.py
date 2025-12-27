# Hindi to English Dictionary
hin_to_eng = {
    'नमस्ते': 'Hello',
    'धन्यवाद': 'Thank you',
    'कृपया': 'Please',
    'हाँ': 'Yes',
    'नहीं': 'No'
}
a = input("एक हिंदी शब्द दर्ज करें(नमस्ते,धन्यवाद,कृपया,हाँ,नहीं): ")
if a in hin_to_eng: #Checking if the word is in the dictionary
    print("अंग्रेजी में:", hin_to_eng[a])
else:
    print("क्षमा करें, यह शब्द उपलब्ध नहीं है।")
