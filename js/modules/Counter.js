import React from 'react';

var origin = window.location.origin;

var Counter = React.createClass({
    incrementCount: function () {
        var world = this
        fetch(origin + '/pokemon/1/add').then(function(response){
            return response.json();
        }).then(function(data){
            world.setState({
                count: data.count,
                pokemon: data.name
            });
        });
    },
    decrementCount: function () {
        this.setState({
            count: this.state.count - 1
        });
    },

    componentDidMount: function() {
        var world = this
        fetch(origin + '/pokemon/1').then(function(response){
            console.log(response)
            return response.json();
        }).then(function(data){
            world.setState({
                count: data.count,
                pokemon: data.name
            });
        });
    },

    getInitialState: function () {
        return {
            count: 0,
            pokemon: ""
        }
    },
    render: function () {
        return (
            <div className="counter">
                <h1>{this.state.count} - Hunting {this.state.pokemon}</h1>
                <button className="btn" onClick={this.incrementCount}>Increment</button>
                <button className="btn" onClick={this.decrementCount}>Decrement</button>
            </div>
        );
    }
});

export default Counter;