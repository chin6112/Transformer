# Transformer Project

## Author

* 66114540366

* นายบรรณวัชร ศรีภักดี

![profile](https://avatars.githubusercontent.com/u/159878397?v=4)
## Project Features

* Django SSE

# AI Agent และ Model Context Protocol (MCP)

## 🔹 AI Agent คืออะไร
**AI Agent** คือ ซอฟต์แวร์หรือโปรแกรมที่ใช้ความสามารถของปัญญาประดิษฐ์ (Artificial Intelligence) เพื่อทำงานแทนมนุษย์บางอย่าง โดยสามารถรับข้อมูล, วิเคราะห์, วางแผน และตัดสินใจเพื่อทำภารกิจได้อย่างอัตโนมัติ

### คุณสมบัติหลักของ AI Agent
1. **การรับรู้ (Perception)**  
   - รับข้อมูลจากสภาพแวดล้อม เช่น ข้อความ, ภาพ, เสียง หรือข้อมูลจาก API  
   - ใช้โมเดล Machine Learning หรือ NLP เพื่อเข้าใจข้อมูล  

2. **การตัดสินใจ (Reasoning / Planning)**  
   - วิเคราะห์ข้อมูลและประเมินสถานการณ์  
   - เลือกแนวทางปฏิบัติที่เหมาะสมที่สุด  

3. **การกระทำ (Action)**  
   - ส่งผลลัพธ์ออกมา เช่น การตอบข้อความ, เรียก API, เขียนไฟล์, สั่งงานหุ่นยนต์  

4. **การเรียนรู้ (Learning)**  
   - ปรับปรุงความสามารถของตนเองจากข้อมูลหรือ feedback  

### ตัวอย่างการใช้งาน AI Agent
- **Chatbot อัจฉริยะ** → ตอบคำถามลูกค้าโดยอัตโนมัติ  
- **ระบบช่วยตัดสินใจ** → วิเคราะห์ข้อมูลธุรกิจและเสนอแนวทาง  
- **Automation Agent** → จัดการงานซ้ำๆ เช่น ส่งอีเมล, อัปเดตฐานข้อมูล  
- **Multimodal Agent** → เข้าใจทั้งข้อความ, รูปภาพ และเสียง  

ℹ️ อ่านเพิ่มเติม: [AWS — What is an AI Agent?](https://aws.amazon.com/what-is/ai-agents/?utm_source=chatgpt.com), [IBM — What Are AI Agents?](https://www.ibm.com/think/topics/ai-agents?utm_source=chatgpt.com), [Wikipedia — Intelligent Agent](https://en.wikipedia.org/wiki/Intelligent_agent?utm_source=chatgpt.com)


---

## 🔹 Model Context Protocol (MCP)
**MCP** (Model Context Protocol) คือ โปรโตคอลมาตรฐานที่ OpenAI และชุมชนเสนอขึ้นมา เพื่อให้ AI Agent สามารถเชื่อมต่อและทำงานร่วมกับ **เครื่องมือ (tools)** หรือ **ระบบภายนอก** ได้ง่ายและปลอดภัย

### จุดประสงค์หลักของ MCP
- กำหนด **มาตรฐานกลาง** สำหรับการแลกเปลี่ยนข้อมูลระหว่าง Agent และระบบอื่น  
- จัดการ **Context** (บริบท) ของการสนทนาและการทำงานของ Agent  
- ลดความซับซ้อนในการเชื่อมต่อ Agent กับ API, Database, หรือบริการต่างๆ  
- ป้องกันปัญหาการเขียน integration ซ้ำซ้อนสำหรับแต่ละเครื่องมือ  

### องค์ประกอบของ MCP
1. **Agent** → ตัวดำเนินการหลักที่ตัดสินใจ  
2. **Client** → ฝั่งที่เรียกใช้งาน Agent หรือให้ input  
3. **Tools / Resources** → ระบบภายนอก เช่น ฐานข้อมูล, API, เครื่องมือวิเคราะห์

ℹ️ อ่านเพิ่มเติม: [OpenAI — MCP Documentation](https://openai.github.io/openai-agents-python/mcp/?utm_source=chatgpt.com), [Microsoft TechCommunity — MCP Integrations](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/model-context-protocol-mcp-integrating-azure-openai-for-enhanced-tool-integratio/4393788?utm_source=chatgpt.com)

---

## 🔹 ความสัมพันธ์ระหว่าง AI Agent และ MCP
- **AI Agent** = "สมอง" → วิเคราะห์ ตัดสินใจ วางแผน  
- **MCP** = "สะพานเชื่อม" → ทำให้ Agent เข้าถึงทรัพยากรและเครื่องมืออื่นได้  
- เมื่อทำงานร่วมกัน → Agent สามารถทำงานที่ซับซ้อนมากขึ้น เช่น  
  - ดึงข้อมูลจากฐานข้อมูล  
  - ประมวลผลด้วย external API  
  - จัดการ workflow ระหว่างหลายระบบ  

---

## 🔹 ตัวอย่างการทำงาน
1. ผู้ใช้พิมพ์คำสั่ง → "ช่วยหาตารางรถไฟเที่ยวถัดไป"  
2. Agent ประมวลผลข้อความ เข้าใจว่าเป็นคำสั่งเกี่ยวกับตารางเวลา  
3. Agent ใช้ MCP เพื่อเชื่อมต่อกับ API ของการรถไฟ  
4. MCP จัดการ context → ส่งข้อมูลที่ถูกต้องให้ Agent  
5. Agent ตอบกลับผู้ใช้ด้วยตารางรถไฟล่าสุด  

---

## 🔹 บทสรุป
- **AI Agent** = ซอฟต์แวร์อัจฉริยะที่ทำงานแทนมนุษย์  
- **MCP** = โปรโตคอลมาตรฐาน ที่ช่วยให้ Agent ใช้งานเครื่องมือและข้อมูลภายนอกได้สะดวก ปลอดภัย และมีประสิทธิภาพ  
- การใช้ AI Agent ร่วมกับ MCP ทำให้สามารถสร้าง **ระบบอัตโนมัติอัจฉริยะ (Intelligent Automation System)** ที่เชื่อมต่อหลายบริการเข้าด้วยกันได้จริง

