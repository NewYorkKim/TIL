import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
// import SQLite from 'react-native-sqlite-storage';
import * as SQLite from 'expo-sqlite';
// import { initDatabaseConfig } from '../configs/SqliteConfig';
import { useState, useEffect } from 'react';

function openDatabase() {
  if (Platform.OS === "web") {
    return {
      transaction: () => {
        return {
          executeSql: () => {},
        };
      },
    };
  }

  const db = SQLite.openDatabase("thesool.db");
  return db;
}

const db = openDatabase();

export default function App() {
  const [items, setItems] = useState(null);

  useEffect(() => {
    db.transaction((tx) => {
      tx.executeSql(
        `SELECT * FROM sul_data;`, 
        [], 
        (_, { rows: {_array} }) => setItems(_array)
      );
    });
  }, []);
  
  return (
    <View style={styles.container}>
      <Text>'Hello'</Text>
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
