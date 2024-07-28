from functionsGPT import comprehend_data

# Note - shortform dummy data below DID NOT WORK with current prompts
data = """Chris is 36 years old and has a French Bulldog called Mabel. He likes to code in his
        spare time. He is working with Josh from Aquinas on this Inversity challenge. They are trying to build
        an MVP to show how AI can read research papers quickly and digest the data.""" # dummy data - PDF will be loaded in here

# Below is a fake research paper I asked ChatGPT to write for testing - this is not real! Had to input a research paper for current prompts
fake_research = """
Title: Exploring the Impact of Artificial Intelligence on Modern Education

Abstract:
This study investigates the transformative impact of artificial intelligence (AI) on modern education. We examine how AI technologies enhance learning experiences, improve educational outcomes, and present challenges and opportunities for educators and students. Through qualitative and quantitative analysis, we provide insights into the current state and future potential of AI in education.

Introduction:
Artificial intelligence (AI) has increasingly become a significant part of various industries, including education. This paper aims to explore the influence of AI on educational practices and outcomes. We discuss the integration of AI tools in classrooms, their benefits, and the associated challenges.

Methodology:
We employed a mixed-methods approach, combining surveys of educators and students with case studies of AI implementations in educational institutions. Data were collected from 100 educators and 500 students across five schools that have integrated AI tools into their curricula.

Results:
The findings indicate that AI positively impacts student engagement and personalized learning. AI-driven platforms, such as adaptive learning systems, have been shown to cater to individual student needs, resulting in improved academic performance. However, challenges such as data privacy concerns and the need for teacher training were also identified.

Discussion:
AI has the potential to revolutionize education by providing personalized learning experiences and automating administrative tasks. Nevertheless, ethical considerations and the digital divide must be addressed to ensure equitable access to AI-enhanced education.

Conclusion:
This study concludes that while AI offers significant benefits for modern education, careful implementation and addressing associated challenges are crucial for maximizing its potential. Future research should focus on long-term impacts and strategies for effective AI integration in education.

Keywords:
Artificial Intelligence, Education, Personalized Learning, Student Engagement, AI Tools, Educational Outcomes

References:

Smith, J. (2020). AI in Education: Opportunities and Challenges. Journal of Educational Technology, 15(2), 123-135.
Doe, A., & Roe, B. (2021). Personalized Learning through AI: A Case Study. International Journal of Learning Technologies, 8(3), 45-59.
Lee, C. (2019). Ethical Implications of AI in Education. Ethics in Technology Review, 12(1), 67-80.
"""

comprehend_data(fake_research)