CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    nickname VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL,
    last_seen TIMESTAMPTZ
);

CREATE TABLE Conversations (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL
);

CREATE TABLE Conversations_users (
    id SERIAL PRIMARY KEY,
    conversation_id INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (conversation_id) REFERENCES Conversations(id),
    FOREIGN KEY (user_id) REFERENCES Users(id)

);

CREATE TABLE Messages (
    id SERIAL PRIMARY KEY,
    conversation_id INT NOT NULL,
    sender_id INT NOT NULL,
    content TEXT NOT NULL,
    sent_at TIMESTAMPTZ DEFAULT NOW() NOT NULL,
    FOREIGN KEY (conversation_id) REFERENCES Conversations(id),
    FOREIGN KEY (sender_id) REFERENCES Users(id)
);
