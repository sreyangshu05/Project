const initialState = {
    chatHistory: [],
    userInput: '',
  };
  
  const chatReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'ADD_MESSAGE':
        return { ...state, chatHistory: [...state.chatHistory, action.payload] };
      case 'SET_USER_INPUT':
        return { ...state, userInput: action.payload };
      case 'LOAD_MESSAGES':
        return state; // Can be modified to load from local storage or an API
      default:
        return state;
    }
  };
  
  export default chatReducer;
  