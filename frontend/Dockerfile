# 1. Immagine di partenza
FROM node:18-alpine

# 2. Cartella di lavoro all'interno del container
WORKDIR /app

# 3. Copia delle dipendenze e installazione
COPY package*.json ./
RUN npm install

# 4. Copia del codice sorgente
COPY . .

# 5. Porta documentata
EXPOSE 3000

# 6. Comando di avvio del container
CMD ["npm", "start"]