import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import React, { useState, useEffect } from "react";
import firebase  from './firebase';

export default function App() {
  const [sulList, setSulList] = useState([]);
  const sulCollection = firebase.collection("sool");
  function getSulDocs () {
    sulCollection.get().then((docs) => {
      var temp = []
      docs.forEach((doc) => {
        temp.push(doc.data());
      });
      setSulList(temp);
      console.log(setSulList);
    });
  }
  useEffect(() => {
    getSulDocs();
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
