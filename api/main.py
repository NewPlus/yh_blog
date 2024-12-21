import uvicorn
from fastapi import FastAPI
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from fastapi.middleware.cors import CORSMiddleware
import os
import json

app = FastAPI()

# CORS 설정
origins = [
    "http://yonghwan.kr.s3-website.ap-northeast-2.amazonaws.com",  # S3 웹사이트 URL
    "http://localhost:3000",  # 로컬 개발 환경의 URL (필요시 추가)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 허용할 출처
    allow_credentials=True,
    allow_methods=["*"],  # 모든 메서드 허용 (GET, POST 등)
    allow_headers=["*"],  # 모든 헤더 허용
)


# AWS S3 클라이언트 설정
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

BUCKET_NAME = 'yonghwan.kr'


@app.get("/blog/posts")
async def get_posts_from_json():
    """JSON 파일에서 블로그 게시물 목록을 가져옵니다."""
    try:
        with open('./blog/posts.json', 'r', encoding='utf-8') as file:
            posts = json.load(file)
        return posts
    except FileNotFoundError:
        return {"error": "JSON 파일을 찾을 수 없습니다."}
    except json.JSONDecodeError:
        return {"error": "JSON 파일을 해석할 수 없습니다."}


@app.get("/blog/post/{post_key}")
async def get_blog_post(post_key: str):
    """S3에서 특정 블로그 게시물의 내용을 가져옵니다."""
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=post_key)
        content = response['Body'].read().decode('utf-8')
        return {"content": content}
    except NoCredentialsError:
        return {"error": "Credentials not available"}

@app.get("/api/posts")
async def get_posts():
    return [
        {"title": "첫 번째 포스트", "content": "이것은 첫 번째 포스트의 내용입니다."},
        {"title": "두 번째 포스트", "content": "이것은 두 번째 포스트의 내용입니다."}
    ]

@app.get("/api/posts_from_s3")
async def get_posts_from_s3():
    """S3에서 블로그 게시물 목록을 가져옵니다."""
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key='posts.json')
        content = response['Body'].read().decode('utf-8')
        posts = json.loads(content)
        return posts
    except NoCredentialsError:
        return {"error": "자격 증명이 없습니다."}
    except ClientError as e:
        return {"error": f"S3 클라이언트 오류: {e}"}
    except json.JSONDecodeError:
        return {"error": "JSON 파일을 해석할 수 없습니다."}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8011)