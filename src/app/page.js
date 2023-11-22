"use client";

import Image from "next/image";
import { useState } from "react";
import { useRouter } from "next/navigation";

export default function Home() {
  const [text, setText] = useState("");
  const router = useRouter();

  const handleSend = async () => {
    try {
      const response = await fetch("/api/processData", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }), // 将textarea中的文本作为JSON数据发送
      });

      if (response.ok) {
        const data = await response.json();
        console.log(data.result); // 打印处理后的结果
      } else {
        console.error("Error:", response.status);
      }
    } catch (error) {
      console.error("Error:", error);
    }
    router.push("/done");
  };
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-800">
      <div className="rounded-full overflow-hidden mb-5 w-50 h-50">
        <Image
          src="/my-img.png"
          alt="My Image"
          width={200}
          height={200}
          className="object-cover"
        />
      </div>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="輸入你的匿名訊息...(50字內)"
        maxLength={50}
        className="mb-4 w-3/4 md:w-1/3 h-48 p-4 text-black rounded-md" // 增加了高度为 h-36，内边距为 p-4
      />
      <button
        onClick={handleSend}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded text-lg" // 增加了内边距为 py-3 px-6，字体大小为 text-lg
      >
        SEND!
      </button>
    </div>
  );
}
