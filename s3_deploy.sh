aws s3 sync ./ s3://yonghwan.kr --profile=default \
  --exclude '*' --include 'blog/*'
