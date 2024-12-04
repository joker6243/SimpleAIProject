import React, {useEffect, useState} from "react";

const App = () => {
    const [message, setMessage] = useState(""); // APIから取得したメッセージを保持
    const [loading, setLoading] = useState(true); // ローディング状態を管理
  
    useEffect(() => {
      fetch("http://localhost:8011/api/data")
        .then((res) => res.json())
        .then((data) => {
          setMessage(data.message);
          setLoading(false);
        })
        .catch((err) => {
          console.error("Error fetching data:", err);
          setLoading(false);
        });
    }, []);
  
    return <h1>{loading ? "Loading..." : message}</h1>; // 状態に応じた表示
  };

export default App;