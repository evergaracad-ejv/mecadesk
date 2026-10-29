FROM node:20-alpine

WORKDIR /app

# Copiar el package.json primero
COPY package.json ./

# Instalar dependencias
RUN npm install

# Copiar el resto del código
COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev"]