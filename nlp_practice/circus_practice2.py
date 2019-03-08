from abc import ABCMeta, abstractmethod
# naming convention
# constant: Uppercase, PI=3.14...


class Animal(metaclass=ABCMeta):

    def __init__(self):
        self.food = ''

    @abstractmethod
    def my_food(self, f=None):
        # 食物種類 = 各Model所需的Dataset
        raise NotImplementedError('food() not implemented.')

    @abstractmethod
    def prepare(self):
        # 準備食物 = 可以看成 Data preprocess / augmentation
        raise NotImplementedError('prepare() not implemented.')

    def eat(self):
        # 吃食物 = 可以看成 Feed dataset
        print('>> [Data Feeding] ' + self.__str__() + ' is eating ' + self.food)

    @abstractmethod
    def perform(self):
        # 動物執行動作 = 執行 forward propagation
        raise NotImplementedError('perform() not implemented.')

    def warn(self):
        # 修正動物錯誤的動作 = 執行 back propagation
        print('>> [Back Prop] Correct {}\'s action'.format(self.__str__()))

    # 動物共同的動作
    def _stand(self):
        print(self.__str__() + ' is standing')

    def _walk(self):
        print(self.__str__() + ' is walking')


class Bear(Animal):

    def __str__(self):
        return 'Bear'

    def my_food(self, f='honey'):
        self.food = f

    def prepare(self):
        # 增加額外的食物 = 做額外的 data augmentation
        self.food += ' + chicken'

    def perform(self):
        # Bear 所可以表演的一系列動作
        print('>> [Forward Prop] starts')
        self._stand()
        self._wave_hands()
        self._walk()
        print('>> [Forward Prop] ends')

    def _wave_hands(self):
        print(self.__str__() + ' is waving hands')


class Tiger(Animal):
    def __str__(self):
        return 'Tiger'

    def my_food(self, f='meat'):
        self.food = f

    def prepare(self):
        # 增加額外的食物 = 做額外的 data augmentation
        self.food += ' + lamb'

    def perform(self):
        # Tiger 所可以表演的一系列動作
        print('>> [Forward Prop] starts')
        self._walk()
        self._jump()
        self._howl()
        print('>> [Forward Prop] ends')

    def _jump(self):
        print(self.__str__() + ' jumped')

    def _howl(self):
        print(self.__str__() + ' is howling')


# 馬戲團是指訓練師
class Circus():
    def __init__(self, animals):
        self.animals = animals

    def __str__(self):
        return 'Circus'

    def _feed(self, animal):
        # 準備食物，即是把每個Batch的資料做預處理或Augmentation
        animal.prepare()
        # 處理完再餵給Model
        animal.eat()

    def train(self, num_training=3):
        # 執行一系列的訓練動作。
        print('-------- Training x {} starts --------'.format(num_training + 1))
        for t in range(num_training): # Epochs
            print('> [{}] Training '.format(t))
            for animal in self.animals:
                self._feed(animal) # get data set
                animal.perform() # forward prop
                animal.warn() # back prop
            print()
        print('-------- Training ends --------')
        print()

    def test(self):
        print('-------- Testing starts --------')
        for animal in self.animals:
            self._feed(animal)  # get data set
            animal.perform()  # forward prop


def main():
    # [1] Prepare = Initialize
    bear = Bear()
    tiger = Tiger()
    bear.my_food('honey')
    tiger.my_food('beef')

    # [2] Training
    animals = [bear, tiger]
    circus = Circus(animals)
    circus.train()

    # [3] Evaluation on a new dataset
    bear.my_food('water')
    tiger.my_food('pork')
    circus.test()


if __name__ == '__main__':
    main()


