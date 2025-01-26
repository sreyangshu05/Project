export const addMessage = (message) => ({
    type: 'ADD_MESSAGE',
    payload: message,
  });
  
  export const setUserInput = (input) => ({
    type: 'SET_USER_INPUT',
    payload: input,
  });
  
  export const loadMessages = () => ({
    type: 'LOAD_MESSAGES',
  });
  