#!/bin/bash

curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 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" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [
      {"role": "user", "content": "Write aparagraph on programing languiage"}
    ]
  }' | jq -r '.choices[0].message.content'
