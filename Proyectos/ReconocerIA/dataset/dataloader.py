import pandas as pd
from torch.utils.data import Dataset
from torchvision.io import read_image
from torch.utils.data import DataLoader
from torchvision import transforms

class EmotionsDataset(Dataset):
    def __init__(self, train_labels: pd.DataFrame, transform=None):
        self.data = pd.read_csv(train_labels)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_path = self.data.iloc[idx, 0]
        img = read_image(img_path) / 255.0
        label = self.data.iloc[idx, 1]

        if img.shape[0] == 1:
            img = img.repeat(3, 1, 1)
        elif img.shape[0] == 4:
            img = img[:3, :, :]
        if self.transform:
            img = self.transform(img)

        return img, label


transform = transforms.Compose([
    transforms.Resize((128,128)),
])
traindataset = EmotionsDataset('train_labels.csv', transform=transform)
trainloader = DataLoader(traindataset,batch_size=32,shuffle=True)