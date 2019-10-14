import React, {Component} from 'react';

class Counter extends Component{
    state = {
        number: 0
    }

    constructor(props){
        super(props);
        console.log('constructor');
    }

    componentWillMount(){
        console.log('componentWillMount (deprecated)');
    }

    componentDidMount(){
        console.log('componentDidMount')
    }

    shouldComponentUpdate(nextProps, nextState){
        console.log('shouldComponentUpdate');
        if(nextState.number % 5 === 0) return false;
        return true;
    }

    componentWillUpdate(nextProps, nextState){
        console.log('componentWillUpdate');
    }


    componentDidUpdate(nextProps, nextState){
        console.log('componentDidUpdate');
    }

    handleIncrease = () =>{
        const {number} = this.state;
        this.setState({
            number: number + 1
        });
    }
    handleDecrease = () =>{
        this.setState(
            ({number}) => ({
            number: number - 1
        })
        );
    }

    render(){
        console.log('render');
        return (
            <div>
                <hi>카운터</hi>
                <div>값: {this.state.number}</div>
                <button onClick={this.handleIncrease}>+</button>
                <button onClick={this.handleDecrease}>-</button>
            </div>
        );
    }        
}

export default Counter;
