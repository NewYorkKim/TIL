import firebase from "firebase/compat/app";
import 'firebase/compat/auth'
import 'firebase/compat/firestore'
import 'firebase/compat/storage'

const firebaseConfig = {
  };
  
  !firebase.apps.length ? firebase.initializeApp(firebaseConfig) : firebase.app()
  
  export default firebase;