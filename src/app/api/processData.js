// pages/api/processData.js

export default async function handler(req, res) {
  if (req.method === "POST") {
    try {
      const { text } = req.body; // 从请求中获取 textarea 中的文本

      // 在这里将文本数据发送给 Python 后端进行处理
      const processedData = await sendDataToPython(text); // 自定义函数，将文本发送给 Python

      // 使用 fetch 或其他 HTTP 请求库发送数据给 Python 后端
      // 这里只是示例，你需要替换为实际的 Python 后端 URL
      const pythonBackendUrl = "http://127.0.0.1:5000/processData"; // 替换为你的 Python 后端 URL
      const response = await fetch(pythonBackendUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: processedData }), // 将处理后的数据发送给 Python 后端
      });

      if (response.ok) {
        const result = await response.json();
        res.status(200).json(result);
      } else {
        console.error("Error:", response.status);
        res.status(500).json({ error: "Internal server error" });
      }
    } catch (error) {
      console.error(error);
      res.status(500).json({ error: "Internal server error" });
    }
  } else {
    res.status(405).end();
  }
}
