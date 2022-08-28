import firebase from "firebase/compat/app";
import 'firebase/compat/auth'
import 'firebase/compat/firestore'
import 'firebase/compat/storage'

const firebaseConfig = {

};
  
const firestoreApp = firebase.initializeApp(firebaseConfig)

export default firestoreApp.firestore();