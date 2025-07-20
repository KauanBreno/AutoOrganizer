# 📁 Organizador de Pastas (Downloads)

Um script simples em Python que organiza automaticamente os arquivos da sua pasta `Downloads`, separando-os por tipo de arquivo (como `.exe`, `.txt`, `.jpg`, etc).

Ideal pra quem quer dar um fim na bagunça da pasta de downloads com um clique só.

---

## 🚀 Como funciona?

1. O script verifica todos os arquivos dentro da sua pasta `Downloads`.
2. Cria pastas com nomes baseados nas extensões definidas (`exe`, `txt`, `jpg`, etc).
3. Move os arquivos para suas respectivas pastas.
4. Cria uma pasta chamada `Arquivos Gerais` para qualquer coisa que não se encaixe nas categorias.

---

## 🧠 Pré-requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa! Só o `pathlib`, que já vem com o Python.

---

## 🛠️ Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd AutoOrganizer
```

### 2. Execute o script de uma das formas abaixo:

#### 👉 Opção 1: Rodar direto pelo VSCode

- Abra o projeto no VSCode.
- Clique com o botão direito no arquivo `Organizando_pastas.py`.
- Selecione **"Run Python File in Terminal"** (ou "Executar Arquivo Python no Terminal").
- Pronto! Ele já vai começar a organizar seus arquivos na pasta Downloads.

#### 👉 Opção 2: Rodar manualmente pelo terminal

Abra o terminal dentro da pasta onde está o script e rode:

```bash
python Organizando_pastas.py
```

#### 👉 Opção 3: Automatizar com o Agendador de Tarefas do Windows

Dá pra deixar o script rodando sozinho todo dia ou toda semana usando o **Agendador de Tarefas do Windows**:

1. Abra o **Agendador de Tarefas**.
2. Crie uma nova tarefa básica.
3. Escolha o horário de execução (diariamente, semanalmente, etc).
4. Quando pedir o programa/script, aponte para o Python, algo como:

   ```text
   C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python3x\python.exe
   ```

5. No campo de argumentos, coloque o caminho completo até seu script:

   ```text
   "C:\caminho\até\seu\projeto\Organizando_pastas.py"
   ```

6. Finalize e... voilá! Seu PC vai se organizar sozinho.

---

## ✍️ Personalização

Quer adicionar mais tipos de arquivos? É só editar essa parte no código:

```python
types = ['exe', 'txt', 'jpg', 'png', 'pdf', 'docx', 'zip']
```

Pode incluir extensões como `'mp3'`, `'mp4'`, `'xlsx'`, `'svg'`, `'pptx'`, etc.

---

## 🤝 Contribuindo

Quer ajudar a melhorar o projeto?  
Fique à vontade pra abrir uma issue ou mandar um pull request.

---

Feito com 💻 por [Kauan Breno](https://github.com/KauanBreno)
