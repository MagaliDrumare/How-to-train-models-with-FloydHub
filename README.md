# A voir et à savoir : 

#### Les solutions de Cloud pour le Deep Learning sont Amazon AWS, Google Cloud et FloydHub. 
* Amazon AWS : offre le plus d'options (https://aws.amazon.com/fr/)
* Google Cloud : plus facile à utiliser que AWS, moins chère (https://cloud.google.com/?hl=fr
* FloydHub: simple, pas chère, solution idéale pour les débutants (https://www.floydhub.com)
* FloyHub on twitter : https://twitter.com/FloydHub_


#### Utiliser FloydHub : 
* Installing Floydhub and running it with TFlearn, Jupyter Notebook, and Tensorboard :https://www.youtube.com/watch?v=byLQ9kgjTdQ
* How to Train Your Models in the Cloud : https://www.youtube.com/watch?v=Bgwujw-yom8


## 1-Entraîner le modèle sur FloydHub : 
> Pré-requis important : placer le fichier NeuralNet dans \Desktop\floyd
> Les instructions suivantes sont à saisir dans la console 
```
Last login: Wed Sep 20 11:00:02 on ttys001
MacBook-Pro-de-DRUMARE:~ magalidrumare$ cd Desktop
MacBook-Pro-de-DRUMARE:Desktop magalidrumare$ cd floyd
MacBook-Pro-de-DRUMARE:floyd magalidrumare$ floyd login
Authentication token page will now open in your browser. Continue? [Y/n]: Y
Please copy and paste the authentication token.
This is an invisible field. Paste token and press ENTER: 
Login Successful
MacBook-Pro-de-DRUMARE:floyd magalidrumare$ floyd run --env tensorflow --gpu "python NeuralNet.py"
```
> Vous devez voir apparaître dans la console 
```
Creating project run. Total upload size: 15.3KiB
Syncing code ...
```
> Pour voir les logs de l'opération vous devez saisir dans la console 
```
To view logs enter:
   floyd logs magalidrumare/projects/my-first-project/3
   ```
   



