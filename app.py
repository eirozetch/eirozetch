from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI  # Import OpenAI class
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Data dummy untuk postingan
POSTS = [
    {
        "id": 1,
        "title": "DeepSeek China Menjadi Ancaman Eksistensial bagi OpenAI dan Google",
        "content": "DeepSeek telah membuat kemajuan pesat dalam mengembangkan solusi AI mutakhir, terutama di bidang pemrosesan bahasa alami, pembelajaran mesin, dan sistem otonom. Inovasi perusahaan ini tidak hanya meningkatkan daya saingnya tetapi juga menantang lanskap AI global, yang selama ini didominasi oleh perusahaan-perusahaan berbasis AS seperti OpenAI (pencipta ChatGPT) dan Google (dengan proyek DeepMind dan Bard-nya). Artikel ini menyoroti bahwa kebangkitan DeepSeek didorong oleh fokus kuat China untuk menjadi pemimpin global dalam teknologi AI. Pemerintah China telah berinvestasi besar-besaran dalam penelitian dan pengembangan AI, menciptakan lingkungan yang mendukung bagi perusahaan seperti DeepSeek untuk berkembang. Dorongan strategis ini merupakan bagian dari tujuan China yang lebih luas untuk mencapai kemandirian teknologi dan mengurangi ketergantungan pada teknologi asing. Selain itu, kemampuan DeepSeek dalam memanfaatkan sumber daya data yang besar di China dan keahliannya dalam algoritma AI memberikan keunggulan tersendiri. Perusahaan ini tidak hanya bersaing di pasar domestik tetapi juga memperluas pengaruhnya secara global, menantang langsung OpenAI dan Google. Artikel ini menyimpulkan bahwa kemunculan DeepSeek menandakan pergeseran dalam dinamika kekuatan AI global. Seiring dengan terus berkembangnya inovasi dan skala perusahaan-perusahaan AI China, mereka berpotensi mengganggu hierarki saat ini di industri teknologi, membuat persaingan semakin intens dan membentuk kembali masa depan pengembangan AI. Sumber: The Economic Times. Chinese DeepSeek is an existential threat to OpenAI and Google. Tersedia di: https://m.economictimes.com/prime/technology-and-startups/chinese-deepseek-is-an-existential-threat-to-openai-and-google/primearticleshow/117594895.cms",
        "image": "post1.jpg"
    },
    {
        "id": 2,
        "title": "Otoritas Perlindungan Data Korea Selatan Menangguhkan Layanan Lokal DeepSeek",
        "content": "Artikel dari The Economic Times melaporkan bahwa otoritas perlindungan data Korea Selatan telah mengambil tindakan terhadap DeepSeek, sebuah perusahaan kecerdasan buatan (AI) asal China, dengan menangguhkan layanan lokalnya di negara tersebut. Keputusan ini muncul karena kekhawatiran atas privasi data dan kepatuhan terhadap undang-undang perlindungan data ketat di Korea Selatan. DeepSeek, yang dikenal dengan teknologi AI mutakhirnya, telah beroperasi di Korea Selatan dengan menawarkan layanan yang sangat bergantung pada pengumpulan dan pemrosesan data. Namun, Komisi Perlindungan Informasi Pribadi Korea Selatan (PIPC) menemukan bahwa praktik DeepSeek tidak sepenuhnya mematuhi peraturan negara tersebut terkait penanganan data pribadi. Secara khusus, PIPC mengangkat masalah tentang bagaimana data pengguna dikumpulkan, disimpan, dan digunakan, terutama terkait persetujuan dan transparansi. Akibatnya, PIPC memerintahkan DeepSeek untuk menangguhkan operasinya di Korea Selatan hingga perusahaan tersebut dapat menunjukkan kepatuhan terhadap undang-undang perlindungan data setempat. Penangguhan ini merupakan kemunduran besar bagi DeepSeek, mengingat Korea Selatan adalah pasar penting untuk teknologi AI, mengingat infrastruktur teknologinya yang maju dan tingkat adopsi layanan digital yang tinggi. Artikel ini menyoroti bahwa insiden ini menegaskan betapa pentingnya privasi dan keamanan data dalam industri AI. Seiring dengan semakin bergantungnya perusahaan AI pada data dalam jumlah besar untuk melatih model dan meningkatkan layanan mereka, mereka harus menavigasi lanskap regulasi yang kompleks di berbagai negara. Kegagalan mematuhi hukum setempat dapat mengakibatkan konsekuensi serius, termasuk penangguhan layanan, denda, dan kerusakan reputasi. Bagi DeepSeek, penangguhan ini tidak hanya memengaruhi operasinya di Korea Selatan tetapi juga memunculkan pertanyaan tentang kemampuannya untuk berekspansi secara global. Seiring dengan semakin ketatnya regulasi perlindungan data di seluruh dunia, perusahaan AI harus memprioritaskan kepatuhan untuk menghindari masalah serupa di pasar lain. Artikel ini menyimpulkan bahwa perkembangan ini mencerminkan ketegangan yang lebih luas di industri teknologi global, terutama antara perusahaan China dan regulator internasional. Saat perusahaan teknologi China seperti DeepSeek berekspansi ke luar negeri, mereka harus menyeimbangkan inovasi dengan kepatuhan terhadap hukum dan peraturan setempat, yang dapat sangat bervariasi dari satu negara ke negara lain. Sumber: The Economic Times. South Korea's Data Protection Authority Suspends Local Service of DeepSeek. Tersedia di: https://m.economictimes.com/tech/artificial-intelligence/south-koreas-data-protection-authority-suspends-local service-of-deepseek/articleshow/118315883.cms",
        "image": "post2.jpg"
    }
]

# Data dummy untuk eBook
EBOOKS = [
    {"id": 1, "title": "TOEFL Preparation Guide 1", "filename": "ebook1.pdf"},
    {"id": 2, "title": "TOEFL Preparation Guide 2", "filename": "ebook2.pdf"},
    {"id": 3, "title": "TOEFL Preparation Guide 3", "filename": "ebook3.pdf"},
    {"id": 4, "title": "TOEFL Preparation Guide 4", "filename": "ebook4.pdf"},
    {"id": 5, "title": "TOEFL Preparation Guide 5", "filename": "ebook5.pdf"}
]

# Load translations
def load_translations(lang):
    import json
    try:
        with open(f"translations/{lang}.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Route untuk halaman utama
@app.route('/')
def home():
    lang = request.args.get('lang', 'id')  # Default language is Indonesian
    translations = load_translations(lang)
    return render_template('index.html', posts=POSTS, lang=lang, translations=translations)

# Route untuk halaman "Tentang Saya"
@app.route('/about')
def about():
    lang = request.args.get('lang', 'id')  # Default language is Indonesian
    translations = load_translations(lang)
    return render_template('about.html', lang=lang, translations=translations)

# Route untuk halaman eBook
@app.route('/ebook')
def ebook():
    lang = request.args.get('lang', 'id')  # Default language is Indonesian
    translations = load_translations(lang)
    return render_template('ebook.html', ebooks=EBOOKS, lang=lang, translations=translations)

# Route untuk halaman detail postingan
@app.route('/post/<int:post_id>')
def post_detail(post_id):
    lang = request.args.get('lang', 'id')  # Default language is Indonesian
    translations = load_translations(lang)
    post = next((post for post in POSTS if post["id"] == post_id), None)
    if post is None:
        return "Postingan tidak ditemukan", 404
    return render_template('post_detail.html', post=post, lang=lang, translations=translations)

# Route untuk halaman chatbot
@app.route('/chatbot')
def chatbot():
    lang = request.args.get('lang', 'id')  # Default language is Indonesian
    translations = load_translations(lang)
    return render_template('chatbot.html', lang=lang, translations=translations)

# Route untuk mendapatkan respons dari API OpenAI (ChatGPT)
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message', '')
    try:
        # Gunakan model gpt-3.5-turbo (ChatGPT versi gratis)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        return jsonify({'response': response.choices[0].message.content})
    except Exception as e:
        return jsonify({'response': f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)