import 'package:flutter/material.dart';

class DetailsScreen extends StatelessWidget {

  int counter;

  DetailsScreen(this.counter);



  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Center(child: Column(
        children: [
          Text("$counter"),
          ElevatedButton(onPressed: () => Navigator.of(context).pop(), child: Text("Go Back"))
        ],
      ),),
    );
  }
}
