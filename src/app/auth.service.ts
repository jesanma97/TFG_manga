import { Injectable } from '@angular/core';
import {AngularFireAuth} from "@angular/fire/auth";

import {Router} from "@angular/router";
import {AngularFirestore} from "@angular/fire/firestore";
import {auth} from "firebase/app";
import {AngularFirestoreDocument} from "@angular/fire/firestore";
import {Observable,of} from "rxjs";
import {switchMap} from "rxjs/operators";
import * as firebase from 'firebase';


@Injectable({
  providedIn: 'root'
})
export class AuthService {
  usuario: any;

  constructor(private AFauth: AngularFireAuth, private router: Router, private db: AngularFirestore) { }




  login(email:string, password: string){

    return new Promise((resolve,rejected) =>{
      this.AFauth.signInWithEmailAndPassword(email,password).then((user) =>{
        const userUid = user.user.uid;
        const datos = {
          colecciones: [],
          volumenes: [],
          pendientes: []
        }
        this.db.collection("manga").doc(userUid).set(datos);
        resolve(user);
        
      }).catch(err => rejected(err));
    })

   

  }

  logout(){
    this.AFauth.signOut().then(() =>{
      this.router.navigate(["/login"]);
    });
  }


  register(email:string, password:string, name:string){

    return new Promise((resolve, reject) =>{
      this.AFauth.createUserWithEmailAndPassword(email,password).then(res =>{
        const uid = res.user.uid;
        this.db.collection("users").doc(uid).set({
          name : name,
          uid : uid,
          email: email,
          password: password
        })
        resolve(res);
      }).catch(err => reject(err));

    })
    

  }




}
