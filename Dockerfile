# Použijeme oficiální Python image (např. python:3.9)
FROM python:3.13

# Proměnné prostředí – zabráníme zápisu bytecode a nastavíme unbuffered output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Nastavíme pracovní adresář
WORKDIR /app

# Zkopírujeme soubor s požadavky a nainstalujeme závislosti
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Zkopírujeme celý projekt do pracovního adresáře
COPY . /app/
