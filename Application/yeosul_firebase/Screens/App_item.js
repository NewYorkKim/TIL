import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Dimensions, Image } from 'react-native';
import React from 'react';

export default function Item({route}) {
    const item = route.params.item
    return (
        <View style={styles.container}>
            <StatusBar style="auto" />
            <Image style={styles.img} source={{uri: item.img}} />
            <Text style={styles.header}>{item.name}</Text>
            <Text style={styles.type}>분류: {item.category}</Text>
            <Text style={styles.material}>주재료: {item.meterial}</Text>
            <Text style={styles.alcohol}>도수: {item.alc}</Text>
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
    header: {
      fontSize: 30,
      marginBottom: 10
    },
    img: {
      flex:0.5,
      aspectRatio: 1.5, 
      resizeMode: 'contain',
      marginBottom: 10
    }
})