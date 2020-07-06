# 
FROM django:latest

# 
LABEL maintainer="eric.ghoubiguian@imerir.com"

# 
COPY . /anovfabmanager

# 
WORKDIR /anovfabmanager

# 
RUN apt upgrade -y && apt update -y

# 
EXPOSE 8000

# 
ENTRYPOINT ["python3", "manage.py", "runserver"]
