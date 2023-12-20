import requests

base_url = 'https://dog.ceo/api'

# Получение списка всех пород собак
def test_get_all_breeds():
    response = requests.get(f"{base_url}/breeds/list/all")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    breeds = data["message"]
    assert len(breeds) > 0

# Получение случайной фотографии собаки
def test_get_random_image():
    response = requests.get(f"{base_url}/breeds/image/random")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    image_url = data["message"]
    assert image_url.startswith("https://images.dog.ceo/breeds/")

# Получение списка подпород для конкретной породы
def test_get_sub_breeds():
    breed = "bulldog"
    response = requests.get(f"{base_url}/breed/{breed}/list")
    assert response.status_code == 200 or response.status_code == 404
    data = response.json()
    if response.status_code == 200:
        assert data["status"] == "success"
        sub_breeds = data["message"]
    else:
        assert data["status"] == "error"
        assert data["message"] == "Breed not found (master breed does not exist)"

# Получение списка изображений для заданной породы
def test_get_breed_images():
    breed = "dane"
    response = requests.get(f"{base_url}/breed/{breed}/images")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    images = data["message"]
    assert len(images) > 0

# Получение случайной фотографии для заданной породы
def test_get_random_breed_image():
    breed = "corgi"
    response = requests.get(f"{base_url}/breed/{breed}/images/random")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    image_url = data["message"]
    assert image_url.startswith("https://images.dog.ceo/breeds/")