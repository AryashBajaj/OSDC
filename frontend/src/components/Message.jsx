import React from "react";
import "../styles/Note.css"

function Message({ message, onDelete }) {
    const formattedDate = new Date(message.created_at).toLocaleDateString("en-US")

    return (
        <div className="">
            <p className="">{message.title}</p>
            <p className="">{message.content}</p>
            <p className="">{formattedDate}</p>
            <button className="" onClick={() => onDelete(message.id)}>
                Delete
            </button>
        </div>
    );
}

export default Message;