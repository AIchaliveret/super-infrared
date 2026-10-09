# AMD AI ACADEMY - RANGKUMAN TRINITY +500 PTS
# Biar gak teledor dan terus mengingat - Untuk AMD AI League

## ONBOARDING 300 PTS (Wajib dulu sebelum ngejar 500)
- [ ] Claim $100 GPU credits di notebooks.amd.com/hackathon (+100)
- [ ] Finish first AMD AI Academy course (+100)
- [ ] Complete AMD profile di account.amd.com/en/profile/preferences.html (+50) -> Sudah kamu lakukan syst!
- [ ] Join lablab Discord + AMD Discord (+50)

## COURSE YANG PALING CEPET BUAT +500 PERTAMA
### 1. ROCm Fundamentals - Open by Design (15 menit)
**Key Takeaway untuk Super-Infrared:**
- ROCm = Radeon Open Compute - alternatif open buat CUDA
- HIP = Heterogeneous-compute Interface for Portability - code CUDA bisa jalan di AMD dengan 1 command hipify
- Kenapa penting: No vendor lock-in, sama kayak yang dipakai Meta & OpenAI 6GW. AT&T pakai Instinct MI355X pakai ROCm 7.2
- Praktik: `amd_check.py` kamu cek `torch.version.hip` - itu ROCm!

### 2. Ryzen AI & AI Edge - Agent Computers: Delegate, Don't Just Operate (20 menit)
**Key Takeaway:**
- Ryzen AI = CPU + GPU + NPU dalam 1 chip - buat edge inference tanpa kirim data sensitif ke cloud
- Pattern: Local AI experiences responsive performance
- Untuk project kamu: Early Guard 612°C & Air Quality 876ppm harus jalan di NPU edge biar 4.7s latency, bukan nunggu cloud
- Hitachi DaaS pakai Ryzen PRO buat scale global - sama kayak rencana deploy sensor kamu

### 3. Instinct MI300X/MI355X - Build AI That Performs at Scale (20 menit)
**Key Takeaway:**
- MI355X: 288GB HBM3E, 8TB/s bandwidth, CDNA 4th Gen - untuk generative AI training, inference, HPC
- TensorWave: 2x performance, 40-60% cost savings vs alternatives pakai MI300X
- AT&T: running full model on single GPU for millions customers - kamu 6 filter agents di 1 GPU
- Praktik: Deploy di Vultr AMD Cloud, pilih instance MI300X

### 4. EPYC & Data Center AI - Confidently Build AI Business Outcomes (15 menit)
**Key Takeaway:**
- EPYC = server CPU buat data center AI, handle concurrent multi-model workloads
- Cisco Healthcare modernize IT infra pakai EPYC - untuk AI-ready operations
- Super-Infrared: Data center on-prem di pabrik pakai EPYC buat aggregator 100 sensor

### 5. Vitis AI & Full-Stack Solutions (20 menit)
**Key Takeaway:**
- Vitis AI = optimize YOLOv5/v8 ke FPGA/Adaptive
- Flow: PyTorch -> ONNX -> Vitis AI quantized -> Deploy di edge
- Untuk kamu: YOLOv5 early fire detection bisa di-quantize biar jalan di Ryzen AI NPU 2W doang

## CARA NGEJAR +500 PTS BIAR GAK TELEDOR
1. Buka academy.amd.com atau lablab AMD Academy Challenge
2. Nonton tiap course 1.5x speed, ambil notes 3 poin penting kayak di atas
3. Kerjain quiz - jangan di-skip, quiz itu yang nge-lock poin
4. Tiap selesai 1 course, screenshot certificate + post di LinkedIn tag #AMDAI #lablab #ROCm -> dapat +10 pts per minggu LinkedIn progress
5. Complete 5 courses = +500 pts (Total onboarding + academy = 800 pts, rank 22 kamu bisa masuk top 10)

## TRINITY CHECKLIST BIAR TERUS MENGINGAT (Setiap hari sebelum coding)
- [ ] **Praktik Code:** Jalanin `python amd_check.py` - apakah masih jalan di Ecosystem atau cuma API?
- [ ] **Praktik Document:** Baca 1 paragraf dari `long_description_ecosystem.md` - apakah masih ingat cerita AT&T/Cisco/Hitachi/TensorWave?
- [ ] **Praktik Academy:** Nonton 1 course 15 menit + tulis 3 takeaway di notes

## NEXT MATCH
- Match 3 RAG (Sep 29-Oct 13): 1,500 pts - Submit Super-Infrared sekarang!
- Match 4 Web Info Retrieval (Oct 13-27): 1,800 pts - Butuh EPYC + ROCm knowledge
- Match 5 Code Repo Repair (Oct 27-Nov 10): 2,100 pts - Butuh Vitis AI + Ryzen AI
- Match 6 Master Unknown (Nov 10-14): 2,400 pts - Full ecosystem

> Ingat syst: Meta.ai bantu rangkum biar paham, tapi tetep harus nonton & klik complete di platform AMD nya sendiri. Jangan joki quiz, itu melanggar. Rangkuman ini legal buat belajar.

Good luck, rank 22 -> Top 3!

