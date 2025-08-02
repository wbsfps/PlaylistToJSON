# 🎵 PlaylistToJSON

Transforme qualquer playlist sua do Spotify em um arquivo JSON com as informações das músicas. Ideal para análise de dados, visualização personalizada ou só para guardar sua seleção de músicas favorita.

---

## 📦 Sobre o projeto

**PlaylistToJSON** é um script Python que autentica via API do Spotify, busca os dados de uma playlist específica e exporta as músicas contidas nela para um arquivo `.json`.

---

## 🚀 Funcionalidades

- ✅ Autenticação com a API do Spotify via Client Credentials
- ✅ Busca completa de uma playlist pública ou sua
- ✅ Extração dos nomes das músicas
- ✅ Exportação estruturada para `.json`

---

## 📁 Estrutura do projeto

```
project-root/
├── src/
│   ├── main.py
│   ├── assets/
│   │   └── musics/
│   │       └── musics.json
│   └── utils/
│       └── send_data_to_json.py
├── services/
│   └── spotify_api/
│       ├── get_token.py
│       ├── get_playlist.py
│       └── get_musics_of_playlist.py
```

---

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/wbsfps/PlaylistToJSON.git
cd PlaylistToJSON
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

> Dependências necessárias: `requests`, `python-dotenv` (se estiver usando variáveis de ambiente)

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz com as seguintes chaves:

```env
CLIENT_ID_SPOTIFY=seu_client_id
CLIENT_SECRET_SPOTIFY=seu_secret_id
PLAYLIST_ID=id_da_sua_playlist
GET_TOKEN_URL_SPOTIFY=https://accounts.spotify.com/api/token
```

### 4. Execute o script

```bash
python -m src.main
```

---

## 📄 Exemplo de saída (`musics.json`)

```json
[
  "Bohemian Rhapsody",
  "Imagine",
  "Stairway to Heaven",
  "Hey Jude",
  "Smells Like Teen Spirit"
]
```

---

## 🧠 Possibilidades futuras

- Adicionar artista e duração de cada música
- Exportar em outros formatos (CSV, XML)
- Criar interface web simples para upload direto
- Análise com pandas para insights da playlist

---

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar!

---

## 🤘 Feito por [William Andrade](https://github.com/wbsfps)
