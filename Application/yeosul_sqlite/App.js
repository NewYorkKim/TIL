import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import SQLite from 'react-native-sqlite-2';

export default function App() {
  const db = SQLite.openDatabase('thesool.db');
  db.transaction(function(txn) {
    txn.executeSql('SELECT * FROM sool_data', [], function(tx, res) {
      for (let i = 0; i < res.rows.length; ++i) {
        console.log('item', res.rows.item(i))
      }
    })
  });

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
