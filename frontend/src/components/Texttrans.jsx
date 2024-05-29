import React, { useState, useEffect } from 'react';
import TextTransition, { presets } from 'react-text-transition';

const TEXTS = ['Where Classroom', 'Begins', 'Communities'];

const TextTransitionComponent = () => {
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(
      () => setIndex((index) => index + 1),
      1000, // every 3 seconds
    );
    return () => clearTimeout(intervalId);
  }, []);

  return (
    <div style={{ position: 'absolute', top: '90px', left: '90px', textAlign: 'center' }}>
    <h1>
      <TextTransition springConfig={presets.wobbly}>{TEXTS[index % TEXTS.length]}</TextTransition>
    </h1>
    </div>
  );
};

export default TextTransitionComponent;