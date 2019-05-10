BÀI TẬP LẬP TRÌNH 1:  ĐO LƯỜNG ĐỘ TƯƠNG TỰ TỰ NGỮ NGHĨA VÀ NHẬN DIỆN QUAN HỆ NGỮ NGHĨA CỦA TỪ SỬ DỤNG WORD EMBEDDINGS

A.	Yêu cầu
Học viên sử dụng ngôn ngữ lập trình python để cài đặt. Khuyến khích học viên cài đặt rõ ràng các hàm chức năng thay vì dùng hàm có sẵn trong các thư viện.
1.	Cài đặt chương trình đo độ tương tự ngữ nghĩa của cặp từ (word similarity) sử dụng pre-trained word embeddings. Sử dụng độ đo khoảng cách Cosine, khoảng cách Dice. Công thức độ đo Cosine và Dice như sau: 
  

Kết quả được đánh giá trên tệp dữ liệu ViCon-400.
2.	Tìm k từ gần nhất với từ w (k từ có khoảng khoảng nhỏ nhất từ vector biểu diễn của chúng đến vector biểu diễn của từ w).
3.	Cài đặt mô hình mạng Logistic Regression hoặc Multi-layer Perceptron để nhận diện cặp từ có quan hệ đồng nghĩa (synonym) và trái nghĩa (antonym) sử dụng bộ dữ liệu ViCon-400 để đánh giá (thư mục Datasets/ViCon-400). 

B.	Dữ liệu  
Học viên được cung cấp dữ liệu tại địa chỉ:
https://github.com/NLP-Projects/Word-Similarity
1.	Bộ pre-trained Word2Vec trong thư mục Word2vec.
Ví dụ, từ “sinh_viên” được biểu diễn bằng một vector 150 chiều như sau: 
sinh_viên -0.16830535 -0.46649584 -0.09095726 0.26220384 -0.06665505 0.031103149 -0.09404702 0.04053062 0.11192394 -0.5279207 0.14246537 0.001038614 -0.35036477 -0.13038214 -0.09090571 0.16573012 -0.36303198 0.09883489 0.18725859 0.13902836 0.06649695 -0.084366314 -0.0027223954 -0.19726162 0.2759428 0.19625933 -0.05050645 -0.2912832 0.3332136 -0.05097548 -0.033659954 0.08438698 0.08262109 0.17202266 0.028343566 -0.2239018 -0.12655334 -0.007960333 -0.11457155 0.05343645 0.04817521 -0.07958502 0.14042595 -0.03268163 0.15085939 -0.019562919 -0.3306483 -0.12484468 0.28407142 0.412389 -0.20573528 0.1886385 -0.32018003 -0.28494123 0.30086038 -0.16913833 -0.15604256 0.014038047 0.0027964886 -0.042381432 0.10412829 -0.25038096 -0.1707933 0.28154066 -0.18622164 -0.12197793 -0.3312451 -0.51899064 -0.30050278 -0.25337204 0.0281554 0.05594583 0.2137868 -0.063191235 -0.25344792 -0.041951556 -0.24166772 -0.06607595 -0.0058164373 0.20314898 0.22446826 -0.27940097 -0.20987804 0.393391 0.19083196 0.1140723 -0.0413766 0.2983006 0.09309805 -0.014998496 0.56122595 -0.21278302 -0.29513258 -0.5796372 -0.104330115 -0.049805988 -0.20145701 0.07974479 -0.08291912 0.20195685 0.5489658 0.27150062 0.28475645 0.047555167 -0.05718565 -0.25075287 0.16845582 -0.26866978 0.24444789 -0.1013144 0.34333876 0.44675854 0.2024813 -0.18543775 -0.428579 0.00044292794 -0.06001611 0.1679784 -0.18539493 0.5264743 0.032929808 -0.11656791 0.11542175 0.345688 -0.16840588 -0.10268665 0.16477033 -0.2467253 0.1251898 0.0076962546 -0.27712318 0.33789232 -0.1583204 0.19434617 -0.23928708 0.177563 0.11510917 0.2388904 -0.50243086 -0.53305346 0.01388552 0.18508705 0.28942367 0.10520081 -0.060460173 0.16218448 0.13140707 -0.16748051 -0.10331021 -0.17137058

2.	Bộ dữ liệu VSim-400 trong thư mục Datasets/ViSim-400.
Một số cặp từ trong bộ dữ liệu VSim-400 được liệt kê dưới đây. Trong đó mỗi dòng gồm 5 thành phần, lần lượt là: từ thứ nhất, từ thứ hai, nhãn từ loại của cặp từ, độ tương tự của cặp từ có giá trị trong khoảng [0,4], độ tương tự của cặp từ được đánh giá trong khoảng [0,6], độ lệch chuẩn của dãy giá trị do 15 chuyên gia đánh giá cặp từ này đưa ra.

Word1		Word2	POS	Sim1	Sim2	STD

biến			ngập		V	3.13	5.22	0.72

động		tĩnh		V	0.6	1.0	0.95

khuyết		ưu		N	0.2	0.33	0.4

cõi_tục		cõi_âm	N	0.6	1.0	0.95

kết_duyên		thành_hôn	V	5.27	8.78	1.06

cấp_tiến		bảo_thủ	A	0.87	1.45	1.15

nước_lớn		nguy_hiểm	N	1.07	1.78	1.12

bất_lợi		thuận_lợi	N	0.33	0.55	0.79

phân_ly		sum_họp	V	0.47	0.78	1.09

diễu_hành		tuần_hành	V	4.53	7.55	1.15

3.	Bộ dữ liệu Vcon-400 tại thư mục Datasets/ViCon-400. 
Một số cặp từ trong bộ dữ liệu VSim-400 được liệt kê dưới đây. Trong đó mỗi dòng gồm ba thành phần, lần lượt là:  từ thứ nhất, từ thứ hai, nhãn quan hệ được gián cho cặp từ. 

Word1		Word2		Relation 

hời_hợt		nông_cạn		SYN

thảnh_thơi		ưu_tư			ANT 

vô_lý		có_lí			ANT 

cuồng_nộ		phẫn_nộ		SYN 

đần			thông_minh		ANT 

có_lí		vô_lí			ANT 

ấm_no		no_ấm		SYN 

lí_thú		lý_thú			SYN 

4.	Tài liệu tham khảo tại thư mục Reference.
