import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import React, { useEffect } from "react";
import { initializeApp } from "firebase/app";
import { getFirestore, collection, getDocs } from "firebase/firestore";

export default function App() {
  const firebaseConfig = {
  };
  const app = initializeApp(firebaseConfig);
  const db = getFirestore(app);
  
  async function getSulData(db) {
    const sulCol = collection(db, 'sool');
    const sulSnapShot = await getDocs(sulCol);
    const sulList = sulSnapShot.docs.map(doc => doc.data());
    console.log(sulList);
  }

  useEffect (() => {
    getSulData(db);
  }, []);

  return (
    <View style={styles.container}>
      <Text>Open up App.js to start working on your app!</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
