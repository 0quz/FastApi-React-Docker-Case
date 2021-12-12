FROM node:16

WORKDIR /case-app

COPY ./package.json ./

COPY ./yarn.lock ./

RUN yarn install

COPY . .

EXPOSE 3000

ENTRYPOINT [ "npm" ]

CMD ["start"]