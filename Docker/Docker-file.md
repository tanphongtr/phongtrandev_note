# Dockerfile Images
## -slim
> Image này chỉ cài đặt các package tối thiểu để chạy
> => Nên sử dụng vì dung lượng thấp mà tương đối đủ các thành phần

## -alpine
> Image này dung lượng thấp nhất, vì không đầy đủ các thành phần nên phải cài thêm, thường sẽ bị lỗi nếu thiếu package

## Full official image (eg: python:3.8.3, node:14.1.1)
> Image này dung lượng lớn, vì các package đầy đủ, thích hợp cho deploy nhanh chóng không cần quan tâm đến những thành phần khác. Tương đối an toàn

# Dockerfile reference
> https://docs.docker.com/engine/reference/builder/

## RUN

## CMD

## ENTRYPOINT

## COPY

## ADD

## EXPOSE

## ARG
